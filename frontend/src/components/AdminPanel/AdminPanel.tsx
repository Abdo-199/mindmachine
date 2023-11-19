import { Card } from "@mui/material";
import CardContent from "@mui/material/CardContent";

import "../../styles/SearchResult/SearchResult.css";
import React from "react"
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import BasicPie from "./PieChart";
import Button from "@mui/material/Button";

import { Grid, Typography, TextField, Box } from "@mui/material";
import { width } from "@mui/system";

function createData(
  Users: string,
  Email: string,
  Storage_usage: number,
  Last_access: Date,
  Status: string
) {
  return { Users, Email, Storage_usage, Last_access, Status };
}
const rows = [
  createData("User01", "s0550199@htw-berlin.de", 65, new Date("10-23-2011"), "User"),
  createData("User02", "s0550299@htw-berlin.de", 93, new Date("11-12-2023"), "Admin"),
  createData("User03", "s0550399@htw-berlin.de", 43, new Date(), "User"),
  
];

const AdminPanel = () => {
  
  return (
    <div>
      <h4 style={{ textAlign:"center" }}>Statistics</h4>
      <h4 style={{ marginLeft: "100px" }}>Storage</h4>
      <Card style={{ marginLeft:100, marginRight:100 }} variant="elevation">
        <CardContent>
          <Grid container>
            {/* First Column */}
            <Grid item xs={12} sm={5}>
              <CardContent>
                <BasicPie></BasicPie>
              </CardContent>
            </Grid>

            {/* Second Column */}
            <Grid item xs={12} sm={7}>
              <Card
                style={{
                  marginLeft: "150px",
                  marginRight: "300px",
                  minWidth: "500px",
                }}
              >
                <h4 style={{textAlign:"center"}}>Storage manager</h4>
                <Grid container style={{maxWidth:"300px"}}>
                  {/* First Row */}
                  <Grid item xs={12} style={{marginLeft:"50px"}}></Grid>
                  Limit storage usage at{" "}
                  <Box component="span" display="inline-block">
                    <TextField
                      sx={{ width: "50px" }}
                      variant="outlined"
                      size="small"
                        
                    />
                  </Box>
                </Grid>
                <Grid container>
                  {/* First Row */}
                  <Grid item xs={12}></Grid>
                  
                  Limit storage usage for every user{" "}
                  <Box component="span" display="inline-block">
                    <TextField
                      sx={{ width: "50px" }}
                      variant="outlined"
                      size="small"
                    />
                  </Box>
                  
                </Grid>
                <Grid container>
                  {/* First Row */}
                  <Grid item xs={12}></Grid>
              
                  <Box >
                  <Button style={{ color : "black" , backgroundColor: "#83b600" , marginLeft:"120px", marginBottom:"15px"}}>Open PDF</Button>
                  </Box>
                </Grid>
              </Card>
            </Grid>
          </Grid>
        </CardContent>
      </Card>

      

      <h4 style={{ marginLeft: "100px", marginTop:"30px"}}>Audio Logout</h4>
      <Card
        style={{ marginLeft: "100px", marginRight: "300px", minWidth: "500px" , marginTop:"20px" }}
      >
        set auto log out after{" "}
        <Box component="span" display="inline-block">
          <TextField sx={{ width: "50px" }} variant="outlined" size="small" />
        </Box>{" "}
        minutes
      </Card>
      <h4 style={{ marginLeft:"100px", marginTop:"30px" }}>Statistics</h4>

      
      
      
      <Card style={{minWidth: "650px" , marginLeft:"100px", marginRight:"100px", marginTop:"20px"}}>
      <TableContainer component={Paper}>
        <Table
          sx={{ minWidth: "650px" , marginLeft:"20px", marginRight:"20px" }}
          aria-label="simple table"
        >
          <TableHead>
            <TableRow >
              <TableCell sx={{ width: '80px' }} align="left" >Users</TableCell>
              <TableCell sx={{ width: '100px' }} align="left">Email</TableCell>
              <TableCell sx={{ width: '30px' }} align="left">User storage</TableCell>
              <TableCell sx={{ width: '30px' }} align="left">Last access</TableCell>
              <TableCell sx={{ width: '30px' }} align="left">Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow>            
                <TableCell align="left">{row.Users}</TableCell>
                <TableCell align="left">{row.Email}</TableCell>
                <TableCell align="left">{row.Storage_usage}</TableCell>
                <TableCell align="left">{row.Last_access.toLocaleDateString()}</TableCell>
                <TableCell align="left">{row.Status}</TableCell>
              </TableRow>
            ))}
          </TableBody>


        </Table>
      </TableContainer>
      </Card>
    </div>
  );
};
export default AdminPanel;
