import { useEffect } from "react";
import "../../styles/Others/Modal.css";
import Modal from "../Others/Modal";

//if you want to delete a file, you see this modal window
const DeleteFileModal = ({
  DeleteFile,
  filename,
  closeModal,
}: {
  DeleteFile: any;
  filename: string | undefined;
  closeModal: any;
}) => {
  
  // let user cancel delete process with escape key
  const handleKeyDown = (event: any) => {
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
        <>
          <hr className="hr-style"></hr>
          <div>
            <span>Do you want to delete the file: {filename}?</span>
            <hr className="hr-style"></hr>
            <div className="renameFileOptions-buttons">
              <button className="fileOption-button" onClick={closeModal}>
                Cancel
              </button>
              <button
                autoFocus
                className="fileOption-button"
                onClick={DeleteFile}
              >
                OK
              </button>
            </div>
          </div>
        </>
      }
      closeModal={closeModal}
    ></Modal>
  );
};

export default DeleteFileModal;
