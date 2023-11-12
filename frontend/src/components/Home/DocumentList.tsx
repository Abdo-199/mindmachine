import DocumentRow from "./DocumentRow";

const DocumentList = ({ docRows }: { docRows: File[] }) => {
  return (
    <>
      <table id="documentList-table">
        <tr id="document-headerRow">
          <th>Name</th>
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
