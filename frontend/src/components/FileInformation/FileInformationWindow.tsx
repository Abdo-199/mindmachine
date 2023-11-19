import "../../styles/FileInformation/FileInformation.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFile } from "@fortawesome/free-solid-svg-icons";
import FileOptions from "./FileOptions";
import FileInfosCard from "./FileInfosCard";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

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
    SearchAndSetObject()
  }, [])

  // Funktion zum Suchen und Setzen des gefundenen Objekts
  const SearchAndSetObject = () => {
    const foundItem = docRows.find(item => item.file_name === filenameParams);

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
          <FileInfosCard file_name={thisFile?.file_name} file_size={thisFile?.file_size} file_date={thisFile?.file_date}></FileInfosCard>
          {thisFile && (
            <FileOptions
              filename={thisFile.file_name}
              SetThisFile={SetThisFile}
              docRows={docRows}
              SetDocRows={SetDocRows}
            ></FileOptions>
          )}
        </div>
      </div>
    </>
  );
};

export default FileInformationWindow;
