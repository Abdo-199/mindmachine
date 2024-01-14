import DocumentRow from "./DocumentRow";

//Table that lists all files
const DocumentList = ({ docRows }: { docRows: File[] }) => {
  return (
    <>
      <table id="documentList-table">
        <tr>
          <th style={{paddingTop: "10px", paddingBottom: "10px"}}>Name</th>
          <th style={{paddingTop: "10px", paddingBottom: "10px"}}>Size</th>
          <th style={{paddingTop: "10px", paddingBottom: "10px"}}>Date</th>
          <th style={{paddingTop: "10px", paddingBottom: "10px"}}>More</th>
        </tr>

        {docRows.map((item, index) => {
          return <DocumentRow key={index} file={item}></DocumentRow>;
        })}
      </table>

      {docRows.length == 0 ? <div style={{display: "flex", justifyContent: "center", marginTop: "20px", fontSize: "1.2rem"}}>No files found!</div> : null}
    </>
  );
};

export default DocumentList;
