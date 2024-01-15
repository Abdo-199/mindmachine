import { useState, useEffect } from "react";
import RenameFileModal from "../Others/RenameFileModal";
import DeleteFileModal from "../Others/DeleteFileModal";
import "../../styles/FileInformation/FileInformation.css";

//Open, rename or delete Card for a file
const FileOptions = ({
  filename,
  SetThisFile,
  docRows,
  SetDocRows,
  ModalHandlerDeleteConfirm,
  fileAlreadyOpen
}: {
  filename: string;
  SetThisFile: any;
  docRows: any[];
  SetDocRows: any;
  fileAlreadyOpen: string
  ModalHandlerDeleteConfirm: any;
}) => {

  //checks, if a filename contains forbidden characters
  function checkFilename(
    inputString: string,
    forbiddenCharacters: RegExp
  ): boolean {
    return forbiddenCharacters.test(inputString);
  }

  const [newFilename, SetNewFilename] = useState("");
  const [isFileOpened, setIsFileOpened] = useState<boolean>(false);
  const [pdfURL, setPDFURL] = useState<string>("");
  const [modalHandlerDataChange, setModalHandlerDataChange] = useState(false);
  const [modalHandlerDataDelete, setModalHandlerDataDelete] = useState(false);
  const [isConfirmed, SetIsConfirmed] = useState(false);

  useEffect(() => {
    if (fileAlreadyOpen == "true") {
      OpenFile()
    }
  }, [])

  // open and close dialog for renaming a file
  const ModalHandlerDataChange = () => {
    setModalHandlerDataChange((current) => !current);
  };

  // open and close dialog for deleting a file
  const ModalHandlerDataDelete = () => {
    setModalHandlerDataDelete((current) => !current);
  };

  // open and close pdf-viewer for displaying a pdf
  const IsFileOpened = () => {
    setIsFileOpened((current) => !current);
  };

  // get pdf file and display it
  const OpenFile = () => {
    IsFileOpened();
    API_GetDocument();
  };

  // rename a file
  const RenameFile = () => {
    if (newFilename == "") {
      return;
    }

    // file name should not consist of any forbidden characters
    const forbiddenCharsRegex = /[\\/?#$"`|^&*:;<>]/;
    if (checkFilename(newFilename, forbiddenCharsRegex)) {
      alert("Input Error. The new filename contains forbidden characters.");
      return;
    }

    // filename will be changed
    SetThisFile((prevFileInfo: any) => ({
      ...prevFileInfo,
      file_name: newFilename,
    }));
    API_EditDocumentName();

    // send confirmation message to user that file has been renamed successfully
    SetIsConfirmed(true);
  };

  // delete a file
  const DeleteFile = () => {
    const fileFound = docRows.find((file) => file.file_name == filename);

    if (fileFound) {
      SetThisFile(null);
      API_DeleteDocument();
      ModalHandlerDeleteConfirm();
    } else {
      alert("Error. There was a problem.");
    }
  };

  // retrieve document from backend
  const API_GetDocument = async () => {
    const fetchString = `${process.env.REACT_APP_production_address}/document?document_name=${filename}`;
    return await fetch(fetchString, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Bearer ${localStorage.getItem("token")}`,
      },
    }).then(async (res) => {
      const blob = await res.blob();
      const pdfUrl = URL.createObjectURL(blob);
      setPDFURL(pdfUrl);
    });
  };

  // send delete request to backend
  const API_DeleteDocument = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/deleteDocument/${filename}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((response) => {
        SetDocRows(docRows.filter((file) => file.file_name !== filename));
      });
  };

  // send rename request to backend
  const API_EditDocumentName = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/editDocumentName`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({ old_name: filename, new_name: newFilename }),
      }
    )
      .then((_response) => {
        const nextList = docRows.map((item) => {
          SetNewFilename("");

          if (item.file_name === filename) {
            item.file_name = newFilename;
            return item;
          } else {
            return item;
          }
        });

        //refresh the docRows with the new named file
        SetDocRows(nextList);
      });
  };

  return (
    <>
      <div id="fileOptions-buttons">
        <button className="fileOption-button" onClick={() => OpenFile()}>
          Open file
        </button>
        <button className="fileOption-button" onClick={ModalHandlerDataChange}>
          Rename
        </button>
        <button className="fileOption-button" onClick={ModalHandlerDataDelete}>
          Delete
        </button>
      </div>
      {modalHandlerDataChange ? (
        <RenameFileModal
          RenameFile={RenameFile}
          isConfirmed={isConfirmed}
          SetIsConfirmed={SetIsConfirmed}
          filename={filename}
          SetNewFilename={SetNewFilename}
          closeModal={ModalHandlerDataChange}
        ></RenameFileModal>
      ) : null}
      {modalHandlerDataDelete ? (
        <DeleteFileModal
          DeleteFile={DeleteFile}
          filename={filename}
          closeModal={ModalHandlerDataDelete}
        ></DeleteFileModal>
      ) : null}
      {isFileOpened && (
        <iframe
          title="pdf-viewer"
          width={"100%"}
          height={"1000"}
          src={pdfURL}
        ></iframe>
      )}
    </>
  );
};

export default FileOptions;
