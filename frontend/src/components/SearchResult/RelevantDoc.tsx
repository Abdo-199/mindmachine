import React from 'react'
import OpenFile from './OpenFile';
import { faCopy } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

interface RelevantDocProps {
    info: { doc_name: string, passage: string, sentence: string };
}

const RelevantDoc: React.FC<RelevantDocProps> = ({ info }) => {
    return (
        <div className="relevant-doc">
            <p className="docName-header">{info.doc_name}</p>
            <hr className="seperator"></hr>

            <div className='paragraphs'>
                <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                    <div style={{ display: "flex", alignItems: "center", columnGap: "15px" }}>
                        <p style={{ fontWeight: "bold" }}>Paragraph</p>
                        <FontAwesomeIcon
                            className='copy-icon'
                            style={{ fontSize: "1.3rem" }}
                            icon={faCopy}
                            onClick={() => { navigator.clipboard.writeText(info.passage) }}
                        ></FontAwesomeIcon>
                    </div>
                    <OpenFile docName={info.doc_name}></OpenFile>
                </div>
                <p>{info.passage}</p>
            </div>

            {info.passage == " " ? <p>No passage found!</p> : null}
        </div>
    )
}

export default RelevantDoc