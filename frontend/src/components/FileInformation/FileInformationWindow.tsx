import "../../styles/FileInformation/FileInformation.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFile } from "@fortawesome/free-solid-svg-icons";
import FileOptions from "./FileOptions";
import FileInfosCard from "./FileInfosCard";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import DeleteFileConfirmModal from "../Others/DeleteFileConfirmModal";

//Is a container for the furhter information of a file
const FileInformationWindow = ({
  docRows,
  SetDocRows,
}: {
  docRows: any[];
  SetDocRows: any;
}) => {
  const { filenameParams, fileAlreadyOpen } = useParams() as { filenameParams: string, fileAlreadyOpen: string };

  //Data that a file contains
  type FileObject = {
    file_name: string;
    file_size: string;
    file_date: string;
  };

  const navigate = useNavigate();

  //The showed file
  const [thisFile, SetThisFile] = useState<FileObject | null>();

  useEffect(() => {
    SearchAndSetObject();
  }, []);

  //Modal for the delete confirmation
  const [modalHandlerDeleteConfirm, SetModalHandlerDeleteConfirm] =
    useState(false);

  const ModalHandlerDeleteConfirm = () => {
    SetModalHandlerDeleteConfirm((current) => !current);
  };

  //Function for searching and setting the found object
  const SearchAndSetObject = () => {
    const foundItem = docRows.find((item) => item.file_name === filenameParams);

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
              ModalHandlerDeleteConfirm={ModalHandlerDeleteConfirm}
              filename={thisFile.file_name}
              SetThisFile={SetThisFile}
              docRows={docRows}
              SetDocRows={SetDocRows}
              fileAlreadyOpen={fileAlreadyOpen}
            ></FileOptions>
          )}
          {modalHandlerDeleteConfirm ? (
            <DeleteFileConfirmModal
              closeModal={() => {
                ModalHandlerDeleteConfirm();
                navigate("/MainWindow");
              }}
            ></DeleteFileConfirmModal>
          ) : null}
        </div>
      </div>
    </>
  );
};

export default FileInformationWindow;
