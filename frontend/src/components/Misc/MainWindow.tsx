import React, { useEffect } from 'react'
import Header from './Header'
import Footer from './Footer'
import HomeWindow from '../Home/HomeWindow'

import '../../styles/Misc/MainWindow.css'
import LegalNotice from './LegalNotice';
import SearchHistory from '../SearchHistory/SearchHistory';
import SearchResult from '../SearchResult/SearchResult';
import AdminPanel from '../AdminPanel/AdminPanel';
import FileInformationWindow from '../FileInformation/FileInformationWindow'
import { useNavigate } from "react-router-dom";

interface MainWindowProps {
  content: string;
}

const MainWindow: React.FC<MainWindowProps> = ({ content }) => {

  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem("userID") == null || localStorage.getItem("isAdmin") == null) {
      navigate("/")
    }
  }, [])

  //Prüfe, was angezeigt werden soll
  var toRenderContent;

  switch (content) {
    case "HomeWindow":
      toRenderContent = <HomeWindow></HomeWindow>
      break;
    case "LegalNotice":
      toRenderContent = <LegalNotice></LegalNotice>
      break;
    case "SearchHistory":
      toRenderContent = <SearchHistory></SearchHistory>
      break;
    case "SearchResult":
      toRenderContent = <SearchResult></SearchResult>
      break;
    case "AdminPanel":
      toRenderContent = <AdminPanel></AdminPanel>
      break;
    case "FileInformation":
      toRenderContent = <FileInformationWindow></FileInformationWindow>
      break;
    default:
      break;
  }


  return (
    <div id="windowWrapper">
      <div id="mainWindow-container">
        <Header></Header>
        <div id="mainContent">
          {toRenderContent}
        </div>
        <Footer></Footer>
      </div>
    </div>
  )
}

export default MainWindow