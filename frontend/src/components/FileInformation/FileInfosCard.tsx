import React, { useState } from "react";
import "../../styles/FileInformation/FileInformation.css";

const FileInfosCard = ({file_name, file_size, file_date}: {file_name: string | undefined, file_size: string | undefined, file_date: string | undefined}) => {
    
  const [size, setSize] = useState("5.3MB");
  const [dateAdded, setDateAdded] = useState("05.11.2023");
  const [description, setDescription] = useState("Blablabla");

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
