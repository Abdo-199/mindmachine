import React, {useState} from 'react'
import { faMicrophone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useNavigate } from "react-router-dom";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

const ConvertVoice = () => {
  
  const navigate = useNavigate();

  const {
    transcript,
    resetTranscript,
    listening,
  } = useSpeechRecognition();

  const [transcriptText, setTranscriptText] = useState(transcript)
  const startListening = () => {
    resetTranscript()
    SpeechRecognition.startListening({ continuous: true, language: "en-GB" });
  };

  const stopListening = async () => {
    setTranscriptText(transcript)
    await SpeechRecognition.stopListening();
  }

  const API_Search = async () => {
    return await fetch(
      `http://141.45.224.114:8000/search?user_id=${localStorage.getItem("userID")}&query=${transcriptText}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => res.json())
      .then((response) => {
        console.log(response)
        //navigate("/SearchResult")
      });
  };

  return (
    <>
      <input id="searchInput" value={listening?transcript : transcriptText} onChange={(e)=>{
        setTranscriptText(e.target.value)
      }} placeholder="Start a search"></input>

      <button id="searchButton" style={{fontSize: "1.3rem"}} onClick={() => API_Search()}>Search</button>

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
