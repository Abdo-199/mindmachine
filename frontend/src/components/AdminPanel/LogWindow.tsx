import {
  Card,
  Input,
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
  // list of all logs that can be filtered
  const [logsList, SetLogsList] = useState<LogProps[]>([]);

  // list of original data
  const [originalLogsList, SetOriginalLogsList] = useState<LogProps[]>([]);

  // get all logs from backend
  const API_GetLogs = async () => {
    const url = `${process.env.REACT_APP_production_address}/logs`;
    console.log(url);
    return await fetch(url, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((response) => {
        // list that will not be changed when filterd
        SetOriginalLogsList(response);
        // list that can be filtered
        SetLogsList(response);
      });
  };

  useEffect(() => {
    API_GetLogs();
  }, []);

  // filter the log table in Date, Event Type and User Action
  const requestSearch = (searched: string) => {
    const displayData = originalLogsList.filter((row) => {
      return (
        row.date.toLowerCase().includes(searched.toLowerCase()) ||
        row.name.toLowerCase().includes(searched.toLowerCase()) ||
        row.message.toLowerCase().includes(searched.toLowerCase())
      );
    });
    SetLogsList(displayData);
  };

  return (
    <div>
      <h1 className="header-center">Log Files</h1>
      <Card
        style={{
          minWidth: "650px",
          marginLeft: "100px",
          marginRight: "100px",
          marginTop: "60px",
          marginBottom: "60px",
        }}
      >

        <div style={{ display: "flex" }}>
          <Input
            style={{ padding: "10px" }}
            placeholder="search Date, Event Type and User Action"
            onChange={(e) => requestSearch(e.target.value)}
            fullWidth
          ></Input>
        </div>

        <TableContainer component={Paper}>
          <Table sx={{ minWidth: "100%" }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell sx={{ width: "20%" }} align="left">
                  Date
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
