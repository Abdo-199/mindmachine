import React from 'react'
import OpenFile from './OpenFile';

interface RelevantDocProps {
    docName: string;
  }
  
  //Other relevant docs, but NOT the most important one
  const RelevantDoc: React.FC<RelevantDocProps> = ({ docName }) => {
    return (
        <div className="relevant-doc">
            <p className="docName-header">{docName}</p>

            <OpenFile docName={docName}></OpenFile>
        </div>
    )
}

export default RelevantDoc