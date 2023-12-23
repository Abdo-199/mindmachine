import "../../styles/FileInformation/FileInformation.css";

//Shows the most important information for a file
const FileInfosCard = ({file_name, file_size, file_date}: {file_name: string | undefined, file_size: string | undefined, file_date: string | undefined}) => {
    
  return (
    <>
      <div id="fileInfosCard">
        <p>
          <span>Filename: </span>
          {file_name}
        </p>
        <p>
          <span>Size: </span>
          {file_size}
        </p>
        <p>
          <span>Date added: </span>
          {file_date}
        </p>
      </div>
    </>
  );
};

export default FileInfosCard;
