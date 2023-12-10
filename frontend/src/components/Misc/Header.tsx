import { useState } from "react";
import "../../styles/Misc/Header.css";
import { useNavigate } from "react-router-dom";
import "react-confirm-alert/src/react-confirm-alert.css"; // Import css
import "../../styles/Misc/MainWindow.css";
import LogoutConfirm from "../Logout/LogoutConfirm";

const Header = () => {
  const navigate = useNavigate();

  const [isAdmin, setIsAdmin] = useState(true);


  return (
    <div id="header-container">
      <div className="header-button" onClick={() => navigate("/MainWindow")}>
        <p>Home</p>
      </div>

      <div className="header-button" onClick={() => navigate("/SearchHistory")}>
        <p>Search History</p>
      </div>

      {isAdmin === true && (
        <div className="header-button" onClick={() => navigate("/AdminPanel")}>
          <p>Admin-Panel</p>
        </div>
      )}
      
      <LogoutConfirm></LogoutConfirm>

    </div>
  );
};

export default Header;
