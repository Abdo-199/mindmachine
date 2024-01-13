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

interface LogProps {
  date: string;
  name: string;
  level: string;
  function: string;
  message: string;
}

const LogWindow = () => {
  // list of all logs
  const [logsList, SetLogsList] = useState<LogProps[]>([]);

  // get all logs from backend
  const API_GetLogs = async () => {
    const url = `${process.env.REACT_APP_production_address}/logs`;
    console.log(url);
    return await fetch(url, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((response) => {
        SetLogsList(response);
      });
  };

  useEffect(() => {
    API_GetLogs();
  }, []);

  return (
    <div>
      <h1 className="header-center">Log Files</h1>
      <Card
        style={{
          minWidth: "650px",
          marginLeft: "100px",
          marginRight: "100px",
          marginTop: "60px",
          marginBottom: "60px"
        }}
      >
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: "100%" }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell sx={{ width: "20%" }} align="left">
                  date
                </TableCell>
                <TableCell align="left">Name</TableCell>
                <TableCell align="left">Level</TableCell>
                <TableCell align="left">Function</TableCell>
                <TableCell align="left">Message</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {logsList.map((line: LogProps) => (
                <TableRow>
                  <TableCell align="left">{line.date.slice(0, -4)}</TableCell>
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