import { useState } from "react";
import RenameFileModal from "../Others/RenameFileModal";
import DeleteFileModal from "../Others/DeleteFileModal";
import "../../styles/FileInformation/FileInformation.css";

const FileOptions = ({
  filename,
  SetThisFile,
  docRows,
  SetDocRows,
  modalHandlerDeleteConfirm,
  ModalHandlerDeleteConfirm,
}: {
  modalHandlerDeleteConfirm: boolean;
  ModalHandlerDeleteConfirm: any;
  filename: string;
  SetThisFile: any;
  docRows: any[];
  SetDocRows: any;
}) => {
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
      SetIsConfirmed(true);
      ModalHandlerDeleteConfirm();
    } else {
      alert("Error. There was a problem.");
    }
  };

  // retrieve document from backend
  const API_GetDocument = async () => {
    const user_id = localStorage.getItem("userID");

    const fetchString = `http://141.45.224.114:8000/document?user_id=${user_id}&document_name=${filename}`;
    return await fetch(fetchString, {
      method: "GET",
    }).then(async (res) => {
      const blob = await res.blob();
      const pdfUrl = URL.createObjectURL(blob);
      console.log(blob);
      console.log(pdfUrl);
      console.log(filename);
      setPDFURL(pdfUrl);
    });
  };

  // send delete request to backend
  const API_DeleteDocument = async () => {
    return await fetch(
      `http://141.45.224.114:8000/deleteDocument/${localStorage.getItem(
        "userID"
      )}/${filename}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        SetDocRows(docRows.filter((file) => file.file_name !== filename));
      });
  };

  // send rename request to backend
  const API_EditDocumentName = async () => {
    return await fetch(
      `http://141.45.224.114:8000/editDocumentName/${localStorage.getItem(
        "userID"
      )}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ old_name: filename, new_name: newFilename }),
      }
    )
      .then((res) => res.json())
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
          isConfirmed={isConfirmed}
          SetIsConfirmed={SetIsConfirmed}
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
