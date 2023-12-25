import React from 'react'
import { useSearchResult } from './SearchResultContext';
import OpenFile from './OpenFile';
import { faCopy } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

//displays information about the most relevant document
const MostRelevantDoc = () => {

    const { searchResult, setSearchResult } = useSearchResult();

    return (
        <div className="relevant-doc">
            <p className="docName-header">{searchResult.relevant_docs[0]}</p>
            <hr className="seperator"></hr>

            <p className="doc-relevant-paragraphs">Relevant paragraphs:</p>

            {/* list of all relevant paragraphs */}
            {searchResult.relevant_paragraphs.map((item: string, index: number) => {
                return <div className='paragraphs'>
                    <div style={{display: "flex", alignItems: "center", columnGap: "15px"}}>
                        <p style={{ fontWeight: "bold"}}>Paragraph {index + 1}</p>
                        <FontAwesomeIcon
                            className='copy-icon'
                            style={{ fontSize: "1.3rem" }}
                            icon={faCopy}
                            onClick={() => {navigator.clipboard.writeText(item)}}
                        ></FontAwesomeIcon>
                    </div>
                    <p>{item}</p>
                </div>
            })}

            {searchResult.relevant_paragraphs[0] == " " ? <p>No paragraphs found!</p> : null}

            <OpenFile docName={searchResult.relevant_docs[0]}></OpenFile>
        </div>
    )
}

export default MostRelevantDoc