import React from "react";
import "../../styles/SearchResult/SearchResult.css";
import SearchInput from "../Home/SearchInput";
import { Alert, AlertTitle } from "@mui/material";
import { useSearchResult } from './SearchResultContext';
import MostRelevantDoc from "./MostRelevantDoc";
import RelevantDoc from "./RelevantDoc";
import { useParams } from "react-router-dom";

//Displays all results of the search
const SearchResult = () => {

  const { searchResult, setSearchResult } = useSearchResult();

  const { query } = useParams() as { query: string };

  return (
    <div id="searchResult-container">
      <SearchInput></SearchInput>

      <p style={{ fontWeight: "bold", fontSize: "1.1rem", marginBottom: "0" }}>Your Question:</p>
      <p>"{query}"</p>


      <MostRelevantDoc></MostRelevantDoc>

      {searchResult.relevant_docs.map((item: string, index: number) => {

        if (index !== 0) {
          return <RelevantDoc docName={item}></RelevantDoc>;
        }
        else { return null; }
      })}

    </div>

  );
};
export default SearchResult;
