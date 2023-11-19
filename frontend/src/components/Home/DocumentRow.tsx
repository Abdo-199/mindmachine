import { Link } from "react-router-dom";

const DocumentRow = ({file}: {file: any}) => {
  // nehme heutiges Datum für Upload-Date
  // const date = new Date().toLocaleDateString()
  // konvertiere bytes in megabytes
  return (
    <tr>
      <td>{file.file_name}</td>
      <td>{file.file_size}</td>
      <td>{file.file_date}</td>
      <td>
        {/* weiterleiten zur File Information Page der jeweiligen Datei*/}
        <Link to={`/FileInformation/${file.file_name}`}>Details</Link>
      </td>
    </tr>
  );
};

export default DocumentRow;
