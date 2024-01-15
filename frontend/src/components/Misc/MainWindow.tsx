import React, { useEffect, useState } from 'react'
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
import { SearchResultProvider } from '../SearchResult/SearchResultContext';
import LogWindow from '../AdminPanel/LogWindow'

interface MainWindowProps {
  content: string;
}

const MainWindow: React.FC<MainWindowProps> = ({ content }) => {

  const navigate = useNavigate();

  //list of all files
  const [docRows, SetDocRows] = useState<any[]>([]);

  //check if user is logged in
  useEffect(() => {
    if (localStorage.getItem("userID") == null || localStorage.getItem("isAdmin") == null) {
      navigate("/")
    }
  }, [])

  //gets from the backend all files
  const GetFileStructure = async () => {
    return await fetch(`${process.env.REACT_APP_production_address}/filestructure`, {
      method: 'GET',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Bearer ${localStorage.getItem("token")}`,
      },
      mode: "cors",
      cache: "no-cache",
    })
      .then(res => res.json())
      .then(response => {
        SetDocRows(response)
      })
  }

  //Check what should be displayed
  const componentMap: { [key: string]: React.ReactElement } = {
    "HomeWindow": <HomeWindow docRows={docRows} SetDocRows={SetDocRows} GetFileStructure={GetFileStructure} />,
    "LegalNotice": <LegalNotice />,
    "SearchHistory": <SearchHistory />,
    "SearchResult": <SearchResult />,
    "AdminPanel": <AdminPanel />,
    "LogWindow": <LogWindow />,
    "FileInformation": <FileInformationWindow docRows={docRows} SetDocRows={SetDocRows} />,
  };

  const toRenderContent = componentMap[content] || <div>Component not found</div>;

  return (
    <div id="windowWrapper">
      <div id="mainWindow-container">
        <Header></Header>
        <div id="mainContent">
          <SearchResultProvider>
            {toRenderContent}
          </SearchResultProvider>
        </div>
        <Footer></Footer>
      </div>
    </div>
  )
}

export default MainWindow