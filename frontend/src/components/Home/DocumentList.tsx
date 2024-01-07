import DocumentRow from "./DocumentRow";

//Table that lists all files
const DocumentList = ({ docRows }: { docRows: File[] }) => {
  return (
    <>
      <table id="documentList-table">
        <tr>
          <th style={{paddingBottom: "10px"}}>Name</th>
          <th>Size</th>
          <th>Date</th>
          <th>More</th>
        </tr>

        {docRows.map((item, index) => {
          return <DocumentRow key={index} file={item}></DocumentRow>;
        })}
      </table>
    </>
  );
};

export default DocumentList;
