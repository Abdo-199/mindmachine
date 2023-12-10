import "../../styles/FileInformation/FileInformation.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFile } from "@fortawesome/free-solid-svg-icons";
import FileOptions from "./FileOptions";
import FileInfosCard from "./FileInfosCard";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Modal from "../Others/Modal";

const FileInformationWindow = ({
  docRows,
  SetDocRows,
}: {
  docRows: any[];
  SetDocRows: any;
}) => {
  const { filenameParams } = useParams() as { filenameParams: string };

  type FileObject = {
    file_name: string;
    file_size: string;
    file_date: string;
  };

  const [thisFile, SetThisFile] = useState<FileObject | null>();

  useEffect(() => {
    SearchAndSetObject();
  }, []);

  const [modalHandlerDeleteConfirm, SetModalHandlerDeleteConfirm] =
    useState(false);

  const ModalHandlerDeleteConfirm = () => {
    // Modalhandler zur Benachrichtigung des Löschvorgangs
    SetModalHandlerDeleteConfirm((current) => !current);
  };

  const navigate = useNavigate();

  // Funktion zum Suchen und Setzen des gefundenen Objekts
  const SearchAndSetObject = () => {
    const foundItem = docRows.find((item) => item.file_name === filenameParams);
    console.log(modalHandlerDeleteConfirm);

    if (foundItem) {
      SetThisFile(foundItem);
    }
  };

  return (
    <>
      <div id="file-information-wrapper">
        <div id="iconCard">
          <FontAwesomeIcon icon={faFile} style={{ fontSize: "9rem" }} />
        </div>
        <div id="fileInfosCard-wrapper">
          <FileInfosCard
            file_name={thisFile?.file_name}
            file_size={thisFile?.file_size}
            file_date={thisFile?.file_date}
          ></FileInfosCard>
          {thisFile && (
            <FileOptions
              modalHandlerDeleteConfirm={modalHandlerDeleteConfirm}
              ModalHandlerDeleteConfirm={ModalHandlerDeleteConfirm}
              filename={thisFile.file_name}
              SetThisFile={SetThisFile}
              docRows={docRows}
              SetDocRows={SetDocRows}
            ></FileOptions>
          )}
          {modalHandlerDeleteConfirm ? (
            <Modal
              header={"Deleting a File"}
              content={
                <div>
                  <hr className="hr-style"></hr>
                  <div>
                    <span>File has been deleted successfully.</span>
                  </div>
                  <br></br>
                  <hr className="hr-style"></hr>
                  <button
                    className="fileOption-button"
                    onClick={() => {
                      ModalHandlerDeleteConfirm();
                      navigate("/MainWindow");
                    }}
                  >
                    OK
                  </button>
                </div>
              }
              closeModal={() => {
                ModalHandlerDeleteConfirm();
                navigate("/MainWindow");
              }}
            ></Modal>
          ) : null}
        </div>
      </div>
    </>
  );
};

export default FileInformationWindow;
