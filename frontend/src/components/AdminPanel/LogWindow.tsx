import {
  Card,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";
import React, { useEffect, useState } from "react";


// test log lines because api route .../logs does not work :'(
const logs_raw = [
  "2024-01-05 15:50:33,715 - INFO - main - [<module>] - Application invoked",
  "2024-01-05 15:50:33,716 - INFO - main - [<module>] - Starting FastAPI server",
  "2024-01-05 15:50:59,135 - INFO - main - [<module>] - Application invoked",
  "2024-01-05 15:50:59,136 - INFO - main - [<module>] - Starting FastAPI server",
];

let logs: LogProps[] = [];

interface LogProps {
  date: string;
  name: string;
  level: string;
  function: string;
  message: string;
}

logs_raw.map((line) => {
  const splittedLine = line.split(" - ");
  logs.push({
    date: splittedLine[0],
    name: splittedLine[1],
    level: splittedLine[2],
    function: splittedLine[3],
    message: splittedLine[4],
  });
});

const LogWindow = () => {
  // list of all logs
  const [logsList, SetLogsList] = useState<LogProps[]>([]);

  // gets all the logs from backend -- does not work now
  const API_GetLogs = async () => {
    const url = `${process.env.REACT_APP_localhost_address}/logs/`;
    console.log(url);
    return await fetch(url, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((response) => {
        console.log(response);
      });
  };

  useEffect(() => {
    // API_GetLogs();
    SetLogsList(logs);
  }, []);

  return (
    <div>
      <h1 className="header-center">Log Files</h1>
      <Card
        style={{
          minWidth: "650px",
          marginLeft: "100px",
          marginRight: "100px",
          marginTop: "20px",
        }}
      >
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: "100%" }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell sx={{ width: "20%" }} align="left">
                  date
                </TableCell>
                <TableCell align="left">name</TableCell>
                <TableCell align="left">level</TableCell>
                <TableCell align="left">function</TableCell>
                <TableCell align="left">message</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {logsList.map((line: LogProps) => (
                <TableRow>
                  <TableCell align="left">{line.date}</TableCell>
                  <TableCell align="left">{line.name}</TableCell>
                  <TableCell align="left">{line.level}</TableCell>
                  <TableCell align="left">{line.function}</TableCell>
                  <TableCell align="left">{line.message}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Card>
    </div>
  );
};

export default LogWindow;