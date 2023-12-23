import { Link } from "react-router-dom";

//One file in the DocumentList (component)
const DocumentRow = ({file}: {file: any}) => {
  return (
    <tr>
      <td>{file.file_name}</td>
      <td>{file.file_size}</td>
      <td>{file.file_date}</td>
      <td>
        <Link to={`/FileInformation/${file.file_name}/false`}>Details</Link>
      </td>
    </tr>
  );
};

export default DocumentRow;
