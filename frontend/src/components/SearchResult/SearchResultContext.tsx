//context for the searchResults

import React, { createContext, useContext, useState, ReactNode } from 'react';

interface SearchResultContextProps {
  children: ReactNode;
}

interface SearchResultContextData {
  searchResult: any; 
  setSearchResult: React.Dispatch<React.SetStateAction<any>>;
}

const SearchResultContext = createContext<SearchResultContextData | undefined>(undefined);

export const SearchResultProvider: React.FC<SearchResultContextProps> = ({ children }) => {
  const [searchResult, setSearchResult] = useState<any>(null);

  return (
    <SearchResultContext.Provider value={{ searchResult, setSearchResult }}>
      {children}
    </SearchResultContext.Provider>
  );
};

export const useSearchResult = (): SearchResultContextData => {
  const context = useContext(SearchResultContext);
  if (!context) {
    throw new Error('useSearchResult must be used within a SearchResultProvider');
  }
  return context;
};
