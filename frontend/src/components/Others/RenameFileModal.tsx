import { useEffect } from "react";
import "../../styles/Others/Modal.css";
import Modal from "../Others/Modal";

//if you want to rename a file, you see this modal window
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

  // let user cancel rename process with escape key
  const handleKeyDown = (event: any) => {
    // close all modals
    if (event.key == "Escape") {
      SetIsConfirmed(false);
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

  // let user rename file with enter key
  const FastRename = (e: any) => {
    if (e.key === "Enter") {
      // wait quarter of second
      // fix for confirm-message dissapearing quickly, because of first enter hit -> better way of solving this problem?
      setTimeout(() => {
        RenameFile();
      }, 250);
    }
  };

  return (
    <Modal
      header={"Renaming a File"}
      closeModal={closeModal}
      content={
        <>
          <hr className="hr-style"></hr>
          {isConfirmed ? (
            <>
              <div>File is renamed successfully to "{filename}".</div>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button
                  autoFocus
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
                    autoFocus
                    onChange={(e) => SetNewFilename(e.target.value + ".pdf")}
                    onKeyDown={(e) => FastRename(e)}
                  ></input>{" "}
                  .pdf
                </span>
              </div>
              <br></br>
              <hr className="hr-style"></hr>
              <div className="renameFileOptions-buttons">
                <button
                  className="fileOption-button"
                  onClick={closeModal}
                >
                  Cancel
                </button>
                <button
                  className="fileOption-button"
                  onClick={RenameFile}
                >
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
