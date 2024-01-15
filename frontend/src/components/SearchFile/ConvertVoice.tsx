import React, { useEffect, useState } from 'react'
import { faMicrophone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useNavigate } from "react-router-dom";
import { useSearchResult } from '../SearchResult/SearchResultContext';
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

const ConvertVoice = () => {

  const navigate = useNavigate();

  //sets the context of the searchResults globally
  const { searchResult, setSearchResult } = useSearchResult();

  const {
    transcript,
    resetTranscript,
    listening,
  } = useSpeechRecognition();

  useEffect(() => {
    const init = () => {
      stopListening()
    }
    init()
  }, [])

  //the written or spoken text
  const [transcriptText, setTranscriptText] = useState(transcript)
  const startListening = () => {
    resetTranscript()
    SpeechRecognition.startListening({ continuous: true, language: "en-GB" });
  };

  const stopListening = async () => {
    setTranscriptText(transcript)
    await SpeechRecognition.stopListening();
  }

  // let user search with enter key
  const FastSearch = (e: any) => {
    if (e.key === "Enter") {
      API_Search();
    }
  };

  //search with qdrant in the backend with the written text (transcript)
  const API_Search = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/search?query=${transcriptText}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      })
      .then((res) => res.json())
      .then((response) => {
        //save the result and navigate to searchResult
        setSearchResult(response)
        navigate(`/SearchResult/${transcriptText}`)
      });
  };
  
  return (
    <>
      <input onKeyDown={(e) => FastSearch(e)} id="searchInput" value={listening ? transcript : transcriptText} onChange={(e)=>{
        setTranscriptText(e.target.value)
      }} placeholder="Start a search"></input>

      <button id="searchButton" style={{ fontSize: "1.3rem" }} onClick={() => API_Search()}>Search</button>

      {listening ? (
        <button id="micButton" style={{ backgroundColor: "red" }}>
          <FontAwesomeIcon
            style={{ fontSize: "1.3rem" }}
            icon={faMicrophone}
            onClick={stopListening}
          ></FontAwesomeIcon>
        </button>
      ) : (
        <button id="micButton">
          <FontAwesomeIcon
            icon={faMicrophone}
            style={{ fontSize: "1.3rem" }}
            onClick={startListening}
          />
        </button>
      )}
    </>
  );
};

export default ConvertVoice;
