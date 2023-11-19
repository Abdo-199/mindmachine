import React, { useState } from 'react'
import '../../styles/Misc/Header.css'
import { useNavigate } from "react-router-dom";

const Header = () => {

    const navigate = useNavigate();

    const [isAdmin, setIsAdmin] = useState(true);

    const LogOut = () => {
        localStorage.removeItem("userID")
        localStorage.removeItem("isAdmin")

        navigate("/")
    }

    return (
        <div id="header-container">
            <div className='header-button' onClick={() => navigate("/MainWindow")}>
                <p>Home</p>
            </div>

            <div className='header-button' onClick={() => navigate("/SearchHistory")}>
                <p>Search History</p>
            </div>

            {isAdmin == true && <div className='header-button' onClick={() => navigate("/AdminPanel")}>
                <p>Admin-Panel</p>
            </div> }

            {/* TODO: LOGOUT */}
            <div className='header-button' onClick={() => LogOut()}>
                <p>Logout</p>
            </div>
        </div>
    )
}

export default Header