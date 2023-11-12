import { useState } from "react";
import "../../styles/Home/Home.css";
import SearchInput from "./SearchInput";
import DocumentList from "./DocumentList";

const HomeWindow = () => {
  // gegenwärtige datei zum Hinzufügen
  const [file, setFile] = useState<File>();
  // Liste aller Dateien (noch nicht user-spezifisch)
  const [docRows, setDocRows] = useState<File[]>([]);

  const selectFiles = (event: any) => {
    for (let i = 0; i < event.target.files.length; i++) {
      const file: File = event.target.files[i];
      // keine Dateien mit doppeltem Namen hochladen 
      if (!docRows.find((x) => x.name == file.name)) {
        setFile(file);
        docRows.push(file);
      }
    }
    setDocRows(docRows)
  };
  return (
    <div className="window-container">
      <SearchInput></SearchInput>
      <h1>Library</h1>
      <label className="custom-file-upload">
        <input
          onChange={selectFiles}
          type="file"
          accept="application/pdf"
          multiple
        />
        Add new files
      </label>
      <DocumentList docRows={docRows}></DocumentList>
    </div>
  );
};

export default HomeWindow;