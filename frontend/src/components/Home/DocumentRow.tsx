import { Link } from "react-router-dom";

const DocumentRow = ({file}: {file: any}) => {
  // nehme heutiges Datum für Upload-Date
  const date = new Date().toLocaleDateString()
  // konvertiere bytes in megabytes
  const size = (file.size/(1024*1024)).toFixed(2)
  return (
    <tr>
      <td>{file.name}</td>
      <td>{size} MB</td>
      <td>{date}</td>
      <td>
        {/* weiterleiten zur File Information Page der jeweiligen Datei*/}
        <Link to={"/"}>details</Link>
      </td>
    </tr>
  );
};

export default DocumentRow;
