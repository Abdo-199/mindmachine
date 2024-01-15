import { useState, ChangeEvent, useEffect } from "react";
import "../../styles/Home/Home.css";
import SearchInput from "./SearchInput";
import DocumentList from "./DocumentList";
import Modal from "../Others/Modal";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faCircleCheck,
  faCircleXmark,
} from "@fortawesome/free-solid-svg-icons";
import LogOutTimer from "../Logout/LogoutTimer";

//The main window (landing page)
const HomeWindow = ({
  docRows,
  SetDocRows,
  GetFileStructure,
}: {
  docRows: any[];
  SetDocRows: any;
  GetFileStructure: () => void;
}) => {

  //modal for the OCR-Check
  const [modalOcrError, setModalOcrError] = useState(false);
  const [modalOcrErrorMessage, setModalOcrErrorMessage] = useState("");

  // display icons indicating status of uploaded file(s)
  const [showUploadIcons, setShowUploadIcons] = useState(false);
  // values indicating whether file is uploaded successfully or not
  const [uploadResponses, setUploadResponses] = useState<boolean[]>([]);

  const [currentMaxUserStorageBytes, setCurrentMaxUserStorageBytes] = useState(0);
  const [storageUsedBytes, setStorageUsedBytes] = useState(0);

  const [currentMaxUserStorageMegabytes, setCurrentMaxUserStorageMegabytes] = useState(0);
  const [storageUsedMegabytes, setStorageUsedMegabytes] = useState(0);

  const [modalNoStroage, setModalNoStorage] = useState(false);

  const [isUploading, setIsUploading] = useState(false);

  useEffect(() => {
    GetFileStructure();
    API_GetMaxUserStorageBytes();
    API_GetStorageUsed();
  }, []);

  useEffect(() => {
    // convertBytesToGigabytes()

    setCurrentMaxUserStorageMegabytes(convertBytesToMegabytes(currentMaxUserStorageBytes))
    setStorageUsedMegabytes(convertBytesToMegabytes(storageUsedBytes))
  }, [storageUsedBytes]);


  //if new file(s) is/are uplaoded...
  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();

    const selectedFiles = event.target.files;
    let flag: boolean = false;

    if (selectedFiles) {
      const formData = new FormData();

      let fileSizes = 0;
      for (let i = 0; i < selectedFiles.length; i++) {
        fileSizes += selectedFiles[i].size
      }

      //Prüfe, ob die fileSizes über dem Wert aus der AdminTable liegen
      if (fileSizes + storageUsedBytes > currentMaxUserStorageBytes) {
        flag = true
        setModalNoStorage(true)
      }

      //Check for forbidden characters
      for (let i = 0; i < selectedFiles.length; i++) {
        if (selectedFiles[i].name.includes("+")) {
          flag = true;
          setModalOcrErrorMessage(
            `File \"${selectedFiles[i].name}\" could not be uploaded. There is a "+" in the file name. `
          );
          setModalOcrError(true);
          break;
        }
        formData.append("files", selectedFiles[i]);
      }

      if (flag == false) {
        API_UploadDocument(formData, selectedFiles);
        setStorageUsedBytes(current => current + fileSizes)
      }
    }
  };

  //Gets the maximum stroage capacity for every user
  const API_GetMaxUserStorageBytes = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/diskusage/user?inBytes=true`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setCurrentMaxUserStorageBytes(response)
      });
  };

  const API_GetStorageUsed = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/current_storage_usage`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setStorageUsedBytes(response)
      });
  };

  const convertBytesToMegabytes = (bytes: any) => {
    return bytes / (1024 * 1024);
  };

  //Uploads the file to the backend
  const API_UploadDocument = async (
    formData: FormData,
    selectedFiles: FileList
  ) => {

    setIsUploading(true)
    setShowUploadIcons(false);

    return await fetch(
      `${process.env.REACT_APP_production_address}/upload`,
      {
        method: "POST",
        headers: {
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
        mode: "cors",
        body: formData,
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setIsUploading(false)
        let error: boolean = false;

        // boolean values indicating success or failure of uploaded files
        let responses: boolean[] = [];
        for (let i = 0; i < response.length; i++) {
          const errorStatus = response[i][1];
          responses.push(errorStatus);

          if (response[i][1] == false) {
            setModalOcrErrorMessage(
              (prevState) =>
                prevState + `File \"${response[i][0]}\" could not be uploaded. `
            );
            error = true;
          }
        }

        setUploadResponses(responses);
        // start displaying status icons
        setShowUploadIcons(true);
        // remove the icon 5 seconds after displaying them
        setTimeout(() => {
          setShowUploadIcons(false);
        }, 10000); // 5000 Millisekunden entsprechen 5 Sekunden

        if (error == true) {
          setModalOcrError(true);
        }

        GetFileStructure();
      });
  };

  return (
    <div className="window-container">
      <SearchInput></SearchInput>
      <h1>Library</h1>
      <div id="file-upload-wrapper">
        <div style={{ display: "flex", alignItems: "center" }}>
          <label className="custom-file-upload">
            <input
              onChange={handleFileChange}
              type="file"
              accept="application/pdf"
              multiple
            />
            Add new files
          </label>

          {isUploading ?
            <div className="loader-container">
              <div className="spinner"></div>
            </div>
            : null}

          {showUploadIcons
            ? uploadResponses.map((status) => {
              return status ? (
                <FontAwesomeIcon id="upload-check-icon" icon={faCircleCheck} />
              ) : (
                <FontAwesomeIcon id="upload-cross-icon" icon={faCircleXmark} />
              );
            })
            : null}
        </div>

        <div id="storage-capacity-wrapper">
          Storage capacity: {storageUsedMegabytes.toFixed(2)} MB / {currentMaxUserStorageMegabytes.toFixed(2)} MB
        </div>
      </div>


      <DocumentList docRows={docRows}></DocumentList>
      <LogOutTimer></LogOutTimer>

      {modalOcrError ? (
        <Modal
          header={"Error"}
          content={
            <div>
              <hr className="hr-style"></hr>
              <div>
                <span>{modalOcrErrorMessage}</span>
              </div>
              <br></br>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button
                  className="fileOption-button"
                  onClick={() => {
                    setModalOcrError(false);
                    setModalOcrErrorMessage("");
                  }}
                >
                  OK
                </button>
              </div>
            </div>
          }
          closeModal={() => {
            setModalOcrError(false);
            setModalOcrErrorMessage("");
          }}
        ></Modal>
      ) : null}


      {modalNoStroage ? (
        <Modal
          header={"Maximum storage space reached!"}
          content={
            <div>
              <hr className="hr-style"></hr>
              <div>
                <span>Please contact the administrator or delete files.</span>
              </div>
              <br></br>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button
                  className="fileOption-button"
                  onClick={() => {
                    setModalNoStorage(false);
                  }}
                >
                  OK
                </button>
              </div>
            </div>
          }
          closeModal={() => {
            setModalNoStorage(false);
          }}
        ></Modal>
      ) : null}
    </div>
  );
};

export default HomeWindow;
