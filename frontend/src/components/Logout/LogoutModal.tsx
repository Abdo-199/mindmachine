import { useEffect } from "react";
import "../../styles/Others/Modal.css";
import Modal from "../Others/Modal";

//Logout confirmation modal window
const LogoutModal = ({
  closeModal,
  Logout,
}: {
  closeModal: any;
  Logout: any;
}) => {
  
  // let user cancel logout process with escape key
  const handleKeyDown = (event: any) => {
    // close logout confirm modal
    if (event.key == "Escape") {
      closeModal();
    }
  };

  // listen for keydown events for this component only
  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  return (
    <Modal
      header={"Logout"}
      content={
        <div>
          <hr className="hr-style"></hr>
          <div>
            <span>Are you sure, you want to leave Mindmachine ?</span>
          </div>
          <br></br>
          <hr className="hr-style"></hr>
          <div className="renameFileOptions-buttons">
            <button className="fileOption-button" onClick={closeModal}>
              Cancel
            </button>
            <button autoFocus className="fileOption-button" onClick={Logout}>
              Confirm
            </button>
          </div>
        </div>
      }
      closeModal={closeModal}
    ></Modal>
  );
};

export default LogoutModal;
