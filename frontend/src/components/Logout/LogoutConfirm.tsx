import { useNavigate } from "react-router-dom";
import { useState } from "react";
import LogoutModal from "./LogoutModal";

//Logout confirmation modal window
const LogoutConfirm = () => {
  const navigate = useNavigate();

  const [modalLogOut, setModalLogOut] = useState(false);

  const logOutModal = () => {
    setModalLogOut((current) => !current);
  };

  //deletes all local storage items
  const handleLogout = () => {
    localStorage.removeItem("userID");
    localStorage.removeItem("isAdmin");
    sessionStorage.removeItem("login_datum");
    navigate("/");
  };
  
  return (
    <>
      {modalLogOut ? (
        <LogoutModal closeModal={logOutModal} Logout={handleLogout}></LogoutModal>
      ) : null}
      <div className="header-button" onClick={() => setModalLogOut(true)}>
        <p>Logout</p>
      </div>
    </>
  );
};

export default LogoutConfirm;
