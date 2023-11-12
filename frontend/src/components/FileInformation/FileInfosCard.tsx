import React, { useState } from 'react'
import '../../styles/FileInformation/FileInformation.css'

const FileInfosCard = () => {

    const [filename, setFileName] = useState("MeinDokument");
    const [size, setSize] = useState("5.3MB");
    const [dateAdded, setDateAdded] = useState("05.11.2023");
    const [description, setDescription] = useState("Blablabla");

  return (
    <div id="fileInfosCard">
        <p><span>Filename: </span>{filename}</p>
        <p><span>Size: </span>{size}</p>
        <p><span>Date added: </span>{dateAdded}</p>
        <p><span>Description: </span>{description}</p>
    </div>
  )
}

export default FileInfosCard