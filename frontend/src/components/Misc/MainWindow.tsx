import React from 'react'
import Header from './Header'
import Footer from './Footer'
import HomeWindow from '../Home/HomeWindow'

import '../../styles/Misc/MainWindow.css'

const MainWindow = () => {
  return (
    <div id="test">


    <div id="mainWindow-container">
        <Header></Header>
        <div id="mainContent">
            <HomeWindow></HomeWindow>
        </div>
        <Footer></Footer>
    </div>
    </div>
  )
}

export default MainWindow