import React from "react";
import "../../styles/Others/Modal.css";
import Modal from "../Others/Modal";

const RenameFileModal = ({
  RenameFile,
  isConfirmed,
  SetIsConfirmed,
  filename,
  SetNewFilename,
  closeModal,
}: {
  RenameFile: any;
  isConfirmed: boolean;
  SetIsConfirmed: any;
  filename: string;
  SetNewFilename: any;
  closeModal: any;
}) => {
  return (
    <Modal
      header={"Renaming a File"}
      closeModal={closeModal}
      content={
        <>
          <hr className="hr-style"></hr>
          {isConfirmed ? (
            <>
              <div>File is renamed successfull to "{filename}".</div>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button
                  className="fileOption-button"
                  onClick={() => {
                    SetIsConfirmed(false);
                    closeModal();
                  }}
                >
                  Ok
                </button>
              </div>
            </>
          ) : (
            <>
              <div>
                <span>Old Filename: {filename}</span>
              </div>
              <br></br>
              <div>
                <span>
                  New Filename:{" "}
                  <input
                    onChange={(e) => SetNewFilename(e.target.value + ".pdf")}
                  ></input>{" "}
                  .pdf
                </span>
              </div>
              <br></br>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button className="fileOption-button" onClick={closeModal}>
                  Cancel
                </button>
                <button className="fileOption-button" onClick={RenameFile}>
                  Save
                </button>
              </div>
            </>
          )}
        </>
      }
    ></Modal>
  );
};

export default RenameFileModal;
