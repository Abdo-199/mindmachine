import "../../styles/Others/Modal.css";

//generic class for the modal window
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
            <div>
              {content}
            </div>
          </div>
          <span className="close" onClick={closeModal}>
            &times;
          </span>
        </div>
      </div>
    </div>
  );
};

export default Modal;
