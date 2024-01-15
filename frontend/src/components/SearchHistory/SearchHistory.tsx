import { useEffect, useState } from "react";
import { useSearchResult } from "../SearchResult/SearchResultContext";
import { useNavigate } from "react-router-dom";
import SearchRow from "./SearchRow";
import "../../styles/SearchHistory/SearchHistory.css";

interface SearchEntryProps {
  query: string;
  date: string;
}

//Table for the history
const SearchHistory = () => {

  const [searchEntries, setSearchEntries] = useState<SearchEntryProps[]>([]);

  const { searchResult, setSearchResult } = useSearchResult();

  const navigate = useNavigate();

  // request to backend to obtain Searchhistory of current user
  const API_GetSearchHistory = async () => {
    const url = `${
      process.env.REACT_APP_production_address
    }/searchhistory`;
    return await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Bearer ${localStorage.getItem("token")}`,
      },
      cache: "no-cache",
    })
      .then((res) => res.json())
      .then((response) => {
        setSearchEntries(response);
      });
  };

  useEffect(() => {
    API_GetSearchHistory();
  }, []);

  // send search request to backend
  const API_Search = async (searchEntryTest: string) => {
    return await fetch(
      `${
        process.env.REACT_APP_production_address
      }/search?query=${searchEntryTest}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setSearchResult(response)
        navigate(`/SearchResult/${searchEntryTest}`);
      });
  };

  const Search = (searchEntry: string) => {
    API_Search(searchEntry);
  };

  // TODO delete a search history entry
  const Delete = (searchEntry: string) => {
    // ...
  };

  return (
    <>
      <div className="outer-search-window">
        <h1 className="header-center">Search History</h1>

        {searchEntries.length == 0 ? (
          <div id="no-search-history">No search history available!</div>
        ) : (
          <table className="search-window" cellSpacing={0} cellPadding={10}>
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
        )}
      </div>
    </>
  );
};

export default SearchHistory;
