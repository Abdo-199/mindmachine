import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import MainWindow from './components/Misc/MainWindow';
import LoginWindow from './components/Login/LoginWindow';
import "./styles/GlobalStyles.css";

import {
  BrowserRouter, Route, Routes
} from 'react-router-dom';

const RouteLayout = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<LoginWindow />} />
      <Route path="/MainWindow" element={<MainWindow content='HomeWindow' />} />
      <Route path="/AdminPanel" element={<MainWindow content='AdminPanel' />} />
      <Route path="/SearchResult" element={<MainWindow content='SearchResult' />} />
      <Route path="/SearchHistory" element={<MainWindow content='SearchHistory' />} />
      <Route path="/FileInformation/:filenameA" element={<MainWindow content='FileInformation' />} />
      <Route path="/LegalNotice" element={<MainWindow content='LegalNotice' />} />
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
