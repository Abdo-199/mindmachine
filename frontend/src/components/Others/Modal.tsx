import React from "react";
import "../../styles/Others/Modal.css";

// Modales Fenster
const Modal = ({
  header,
  closeModal,
  content,
}: {
  header: string;
  closeModal: any;
  content: any;
}) => {
  return (
    <div className="modal">
      <div className="modal-content">
        <div className="container">
          <div style={{width: "90%"}}>
            <h1>
              {header}
            </h1>
            {/* <Header title={header} fontSize={"1.5rem"}></Header> */}
            <div>
              {content} {/* An diese Stelle kommt der Inhalt hin */}
            </div>
          </div>
          <span className="close" onClick={() => closeModal()}>
            &times;
          </span>
        </div>
      </div>
    </div>
  );
};

export default Modal;
