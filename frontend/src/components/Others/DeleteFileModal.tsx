import React from "react";
import "../../styles/Others/Modal.css";
import Modal from "../Others/Modal";

const DeleteFileModal = ({
  DeleteFile,
  isConfirmed,
  SetIsConfirmed,
  filename,
  closeModal,
}: {
  DeleteFile: any;
  isConfirmed: boolean;
  SetIsConfirmed: any;
  filename: string | undefined;
  closeModal: any;
}) => {

  return (
    <Modal
      header={"Deleting a File"}
      content={
        <>
          <hr className="hr-style"></hr>
          {isConfirmed ? (
            <>
              <span>"{filename}" is deleted successfully.</span>
              <button
                className="fileOption-button"
                onClick={() => {
                    closeModal();
                    SetIsConfirmed(false);
                }}
              >
                OK
              </button>
            </>
          ) : (
            <div>
              <span>Do you want to delete the file: {filename}?</span>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button className="fileOption-button" onClick={closeModal}>
                  Cancel
                </button>
                <button className="fileOption-button" onClick={DeleteFile}>
                  OK
                </button>
              </div>
            </div>
          )}
        </>
      }
      closeModal={closeModal}
    ></Modal>
  );
};

export default DeleteFileModal;
