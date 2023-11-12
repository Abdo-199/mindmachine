import React from 'react'
import '../../styles/FileInformation/FileInformation.css'

const FileOptions = () => {

    const RenameFile = () => {

    }

    const DeleteFile = () => {

    }
    
    return (
        <div id="fileOptions-buttons">
            <button className='fileOption-button' onClick={() => console.log("Open")}>Open file</button>
            <button className='fileOption-button' onClick={() => RenameFile()}>Rename</button>
            <button className='fileOption-button' onClick={() => DeleteFile()}>Delete</button>
        </div>
    )
}

export default FileOptions