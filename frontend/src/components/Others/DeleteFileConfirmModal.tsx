import { useEffect } from "react";
import "../../styles/Others/Modal.css";
import Modal from "./Modal";

//if you want to delete a file and confirm, you see this modal window
const DeleteFileConfirmModal = ({ closeModal }: { closeModal: any }) => {

  // let user cancel delete process with escape key
  const handleKeyDown = (event: any) => {
    // close delete confirm modal
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
      header={"Deleting a File"}
      content={
        <div>
          <hr className="hr-style"></hr>
          <div>
            <span>File has been deleted successfully.</span>
          </div>
          <br></br>
          <hr className="hr-style"></hr>
          <button autoFocus className="fileOption-button" onClick={closeModal}>
            OK
          </button>
        </div>
      }
      closeModal={closeModal}
    ></Modal>
  );
};

export default DeleteFileConfirmModal;
