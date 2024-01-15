import "../../styles/SearchHistory/SearchHistory.css";

interface SearchRowProps {
  name: string;
  createdOn: string;
  Search: any;
  Delete: any;
}

//is one history item (one old search)
const SearchRow = ({ name, createdOn, Search, Delete }: SearchRowProps) => {
  const date = new Date(createdOn).toLocaleDateString();
  
  return (
    <tr>
      <td>{name}</td>
      <td>{date}</td>
      <td>
        <button style={{float: "right", marginRight: "20px"}} onClick={() => Search(name)}>Search</button>
      </td>
    </tr>
  );
};

export default SearchRow;
