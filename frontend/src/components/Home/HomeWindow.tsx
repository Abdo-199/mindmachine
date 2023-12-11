import { useState, ChangeEvent, useEffect } from "react";
import "../../styles/Home/Home.css";
import SearchInput from "./SearchInput";
import DocumentList from "./DocumentList";
import Modal from "../Others/Modal";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleCheck } from "@fortawesome/free-solid-svg-icons";

const HomeWindow = ({
  docRows,
  SetDocRows,
  GetFileStructure,
}: {
  docRows: any[];
  SetDocRows: any;
  GetFileStructure: () => void;
}) => {

  const [modalOcrError, setModalOcrError] = useState(false);
  const [modalOcrErrorMessage, setModalOcrErrorMessage] = useState("");
  const [showCheckIcon, setShowCheckIcon] = useState(false);

  useEffect(() => {
    GetFileStructure();
  }, []);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();

    const selectedFiles = event.target.files;

    if (selectedFiles) {
      //setFiles(selectedFiles);
      const formData = new FormData();

      for (let i = 0; i < selectedFiles.length; i++) {
        formData.append("files", selectedFiles[i]);
      }

      API_UploadDocument(formData, selectedFiles);
    }
  };

  const API_UploadDocument = async (
    formData: FormData,
    selectedFiles: FileList
  ) => {
    return await fetch(
      `http://141.45.224.114:8000/upload/${localStorage.getItem("userID")}`,
      {
        method: "POST",
        mode: "cors",
        body: formData,
      }
    )
      .then((res) => res.json())
      .then((response) => {
        console.log(response)

        let error:boolean = false;
        for (let i = 0; i < response.length; i++) {
          if (response[i][1] == false) {
            setModalOcrErrorMessage(prevState => prevState + `File \"${response[i][0]}\" could not be uploaded.`)
            error = true;
          }
        }

        if (error == true) {
          setModalOcrError(true)
        }
        else {
          setShowCheckIcon(true)
          setTimeout(() => {
            setShowCheckIcon(false)
          }, 5000); // 5000 Millisekunden entsprechen 5 Sekunden
        }

        GetFileStructure();
      });
  };

  return (
    <div className="window-container">
      <SearchInput></SearchInput>
      <h1>Library</h1>
      <div id="file-upload-wrapper">
        <label className="custom-file-upload">
          <input
            onChange={handleFileChange}
            type="file"
            accept="application/pdf"
            multiple
          />
          Add new files
        </label>
    	  {showCheckIcon ? <FontAwesomeIcon id="upload-check-icon" icon={faCircleCheck}/> : null}
      </div>

      <DocumentList docRows={docRows}></DocumentList>

      {modalOcrError ? (
        <Modal
          header={"Fehler"}
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
                  onClick={() => setModalOcrError(false)}>
                  OK
                </button>
              </div>
            </div>
          }
          closeModal={() => setModalOcrError(false)}
        ></Modal>
      ) : null}
    </div>
  );
};

export default HomeWindow;
