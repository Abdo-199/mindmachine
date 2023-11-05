import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import MainWindow from './components/Misc/MainWindow';
import LoginWindow from './components/Login/LoginWindow';
import "./styles/GlobalStyles.css";

import {
  BrowserRouter, Route, Routes
} from 'react-router-dom';


import AdminPanel from './components/AdminPanel/AdminPanel';
import FileInformation from './components/FileInformation/FileInformation';
import SearchHistory from './components/SearchHistory/SearchHistory';
import SearchResult from './components/SearchResult/SearchResult';

const RouteLayout = () => (

  <BrowserRouter>
    
    <Routes>
      <Route path="/" element={<LoginWindow  />} />
      <Route path="/MainWindow" element={<MainWindow  />} />
      <Route path="/AdminPanel" element={<AdminPanel />} />
      <Route path="/SearchResult" element={<SearchResult  />} />
      <Route path="/SearchHistory" element={<SearchHistory />} />
      <Route path="/FileInformation" element={<FileInformation  />} />
    </Routes>
    </BrowserRouter>
);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
    <div>
      <RouteLayout></RouteLayout>
    </div>
);




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
