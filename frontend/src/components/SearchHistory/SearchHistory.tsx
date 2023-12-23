import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSearchResult } from "../SearchResult/SearchResultContext";
import SearchRow from "./SearchRow";
import "../../styles/SearchHistory/SearchHistory.css";

interface SearchEntryProps {
  query: string;
  date: string;
}

const SearchHistory = () => {
  const [searchEntries, setSearchEntries] = useState<SearchEntryProps[]>([]);

  // request to backend to obtain Searchhistory of current user
  const API_GetSearchHistory = async () => {
    const url = `${
      process.env.REACT_APP_production_address
    }/searchhistory/${localStorage.getItem("userID")}`;
    return await fetch(url, {
      method: "GET",
      mode: "cors",
      cache: "no-cache",
    })
      .then((res) => res.json())
      .then((response) => {
        console.log(response);
        setSearchEntries(response);
      });
  };

  useEffect(() => {
    API_GetSearchHistory();
  }, []);
  
  const Search = (searchEntry: string) => {

  };

  // TODO delete a search history entry
  const Delete = (searchEntry: string) => {
    // ...
  };

  return (
    <>
      <div className="outer-search-window">
        <h1 className="header-center">Search History</h1>
        {/* <table className="searchEntries-table"> */}
        <table className="search-window">
          {searchEntries.map((entry, index) => (
            <SearchRow
              key={index}
              name={entry.query}
              createdOn={entry.date}
              Search={Search}
              Delete={Delete}
            ></SearchRow>
          ))}
        </table>
      </div>
    </>
  );
};

export default SearchHistory;
