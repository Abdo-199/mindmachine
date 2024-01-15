import React, { useEffect } from "react";
import "../../styles/SearchResult/SearchResult.css";
import SearchInput from "../Home/SearchInput";
import { useSearchResult } from './SearchResultContext';
import RelevantDoc from "./RelevantDoc";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

//Displays all results of the search
const SearchResult = () => {

  const navigate = useNavigate();
  const { searchResult, setSearchResult } = useSearchResult();

  const { query } = useParams() as { query: string };

  useEffect(() => {
    if (searchResult == null) {
      navigate("/MainWindow")
    }
  }, [])

  return (
    <div id="searchResult-container">
      <SearchInput></SearchInput>

      <p style={{ fontWeight: "bold", fontSize: "1.1rem", marginBottom: "0" }}>Your Question:</p>
      <p>"{query}"</p>

      {searchResult != null ? searchResult.map((info: { doc_name: string, passage: string, sentence: string }, index: number) => {
        return <RelevantDoc info={info}></RelevantDoc>
      }) : null}
    </div>

  );
};
export default SearchResult;
