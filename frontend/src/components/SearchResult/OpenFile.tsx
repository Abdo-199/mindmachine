import React from 'react'
import { Link } from "react-router-dom";
import "../../styles/SearchResult/SearchResult.css"

interface RelevantDocProps {
  docName: string;
}

//Link to open the file
const OpenFile: React.FC<RelevantDocProps> = ({ docName }) => {

  return (
    <button className='button-openfile' style={{float: "right"}}>
      <Link to={`/FileInformation/${docName}/true`} style={{ textDecoration: "none", color: "black" }}>Open File</Link>
    </button>
  )
}

export default OpenFile