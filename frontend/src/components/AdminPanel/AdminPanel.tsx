import { Card } from "@mui/material";
import CardContent from "@mui/material/CardContent";
import "../../styles/SearchResult/SearchResult.css";
import React, { useState, useEffect } from "react"
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { Grid, TextField, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import Modal from "../Others/Modal";

function createData(
  Users: string,
  Email: string,
  Storage_usage: number,
  Last_access: Date,
  Status: string
) {
  return { Users, Email, Storage_usage, Last_access, Status };
}

interface Statistics {
  user_id: string;
  is_admin: boolean;
  used_storage: string;
  last_login: Date;
}

const AdminPanel = () => {

  const navigate = useNavigate();

  const [currentLogoutTime, setCurrentLogoutTime] = useState("");
  const [newLogoutTime, setNewLogoutTime] = useState("");
  const [showErrorNewLogoutTime, setShowErrorNewLogoutTime] = useState(false);

  const [currentMaxUserStorage, setCurrentMaxUserStorage] = useState("");
  const [newMaxUserStorage, setNewMaxUserStorage] = useState("");
  const [showErrorNewMaxUserStorage, setShowErrorNewMaxUserStorage] = useState(false);

  const [globalStorageUsage, setGlobalStorageUsage] = useState("");

  const [statistics, setStatistics] = useState([]);
  const [activeUsers, setActiveUsers] = useState(0)

  useEffect(() => {
    API_GetLogoutTime();
    API_GetMaxUserStorage();
    API_GetGlobalStorageUsage();
    API_GetStatistics();

    if (localStorage.getItem("isAdmin") == "false") {
      navigate("/")
    }
  }, []);

  const API_GetLogoutTime = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/autologout`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setCurrentLogoutTime(response)
      });
  };

  const handleChangeLogoutTime = (event: any) => {
    setNewLogoutTime(event.target.value);
  };

  const handleChangeUserStorage = (event: any) => {
    setNewMaxUserStorage(event.target.value);
  };

  const API_SetLogoutTime = async () => {

    if (newLogoutTime != "") {
      return await fetch(
        `${process.env.REACT_APP_production_address}/autologout?logout_timer=${newLogoutTime}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            'Authorization': `Bearer ${localStorage.getItem("token")}`,
          },
        }
      )
        .then((res) => res.json())
        .then((response) => {
          setCurrentLogoutTime(newLogoutTime)
          ModalHandlerChangeLogoutTime()
          setNewLogoutTime("")
          setShowErrorNewLogoutTime(false)
        });
    }
    else {
      setShowErrorNewLogoutTime(true)
    }
  };

  //Gets the maximum stroage capacity for every user
  const API_GetMaxUserStorage = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/diskusage/user?inBytes=false`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setCurrentMaxUserStorage(response)
      });
  };

  const convertToBytes = () => {
    const gigabytes = parseFloat(newMaxUserStorage);
    if (!isNaN(gigabytes)) {
      const bytes = gigabytes * Math.pow(1024, 3); // 1 GB = 1024^3 Bytes
      return bytes;
    } else {
      return null;
    }
  };

  const [modalHandlerChangeMaxUserStorage, setModalHandlerChangeMaxUserStorage] = useState(false);
  const ModalHandlerChangeMaxUserStorage = () => {
    setModalHandlerChangeMaxUserStorage((current) => !current);
  };

  const [modalHandlerChangeLogoutTime, setModalHandlerChangeLogoutTime] = useState(false);
  const ModalHandlerChangeLogoutTime = () => {
    setModalHandlerChangeLogoutTime((current) => !current);
  };

  const API_ChangeMaxUserStorage = async () => {

    let bytes = convertToBytes();

    if (bytes == null) {
      setShowErrorNewMaxUserStorage(true)
      return;
    }

    return await fetch(
      `${process.env.REACT_APP_production_address}/diskusage/user?disk_usage=${bytes}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setCurrentMaxUserStorage(newMaxUserStorage + " GB")
        ModalHandlerChangeMaxUserStorage()
        setNewMaxUserStorage("")
        setShowErrorNewMaxUserStorage(false)
      });
  };

  const API_GetGlobalStorageUsage = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/storage_usage`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setGlobalStorageUsage(response)
      });
  };

  const API_GetStatistics = async () => {
    return await fetch(
      `${process.env.REACT_APP_production_address}/statistics`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((response) => {
        setStatistics(response.statistics)
        setActiveUsers(response.activeUsers)
      });
  };

  function RenderDate(last_login: Date) {
    const dateObject = new Date(last_login);
    const options = { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' };
    return dateObject.toLocaleString('de-DE');
  }

  return (
    <div>
      <h1 className="header-center">Admin Panel</h1>


      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h4 style={{ marginLeft: "100px", width: "50%"}}>Storage</h4>
        <h4 style={{ marginRight: "30px", width: "50%" }}>Auto Logout</h4>
      </div>


      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <Card style={{ marginLeft: 100, marginRight: 50, width: "50%" }} variant="elevation">
          <CardContent>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginRight: "50px" }}>

              <div style={{ fontSize: "2rem", fontWeight: "bold", marginLeft: "30px" }}>
                {globalStorageUsage}
              </div>

              <Grid>
                <Grid container style={{ display: "flex", columnGap: "8px", alignItems: "center" }}>

                  Limit storage usage for every user:
                  <Box component="span" display="inline-block">
                    <TextField
                      variant="outlined"
                      size="small"
                      type="number"
                      onChange={handleChangeUserStorage}
                      placeholder="1"
                      error={newMaxUserStorage === "" && showErrorNewMaxUserStorage}
                      value={newMaxUserStorage}
                      sx={{ width: "70px" }} style={{ height: "0px", maxHeight: "20px", marginBottom: "30px" }}
                    />
                  </Box>
                  GB
                </Grid>

                Current: {currentMaxUserStorage}
                <Grid>
                  <Box>
                    <Button onClick={() => API_ChangeMaxUserStorage()} style={{ color: "black", backgroundColor: "#83b600", marginLeft: "120px", marginBottom: "15px", marginTop: "50px" }}>Change storage</Button>
                  </Box>
                </Grid>

              </Grid>
            </div>
          </CardContent>
        </Card>

        <Card
          style={{
            display: "flex",
            alignItems: "center",
            flexDirection: "column",
            justifyContent: "space-between",
            columnGap: "10px",
            marginLeft: "50px",
            marginRight: "100px",
            padding: "15px",
            width: "50%",
            paddingTop: "30px",
            paddingBottom: "40px"
          }}>
          <div style={{ display: "flex", alignItems: "center", columnGap: "10px" }}>
            Set auto logout after{""}
            <Box component="span" display="inline-block" style={{ justifySelf: "flex-start" }}>
              <TextField error={newLogoutTime === "" && showErrorNewLogoutTime} value={newLogoutTime} onChange={handleChangeLogoutTime} sx={{ width: "70px", marginBottom: "35px" }} style={{ height: "0px", maxHeight: "20px" }} variant="outlined" size="small" placeholder="60" type="number" />
            </Box>{" "}
            minutes. Current is {currentLogoutTime} minutes.
          </div>
          <Button style={{ color: "black", backgroundColor: "#83b600" }} onClick={() => API_SetLogoutTime()}>Change logout time</Button>
        </Card>
      </div>


      <h4 style={{ marginLeft: "100px", marginTop: "30px" }}>Log files</h4>
      <Card
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          columnGap: "10px",
          marginLeft: "100px",
          marginRight: "100px",
          padding: "15px",
          minWidth: "500px",
          marginTop: "20px"
        }}>

        <Button style={{ color: "black", backgroundColor: "#83b600" }} onClick={() => navigate("/LogWindow")}>Go to log files</Button>
      </Card>



      <h4 style={{ marginLeft: "100px", marginTop: "30px" }}>Statistics</h4>

      <p style={{ marginLeft: "100px" }}>Active users: {activeUsers}</p>
      <Card style={{ minWidth: "650px", marginLeft: "100px", marginRight: "100px", marginTop: "20px" }}>
        <TableContainer component={Paper}>
          <Table
            sx={{ minWidth: "100%" }}
            aria-label="simple table"
          >
            <TableHead>
              <TableRow>
                <TableCell sx={{ width: '80px' }} align="left" >User</TableCell>
                <TableCell sx={{ width: '100px' }} align="left">Email</TableCell>
                <TableCell sx={{ width: '30px' }} align="left">Used storage</TableCell>
                <TableCell sx={{ width: '30px' }} align="left">Last access</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {statistics.length != 0 ? statistics.map((row: Statistics) => (
                <TableRow>
                  <TableCell align="left">{row.user_id}</TableCell>
                  <TableCell align="left">{row.user_id.startsWith("s0") ? row.user_id + "@htw-berlin.de" : null}</TableCell>
                  <TableCell align="left">{row.used_storage}</TableCell>
                  <TableCell align="left">{RenderDate(row.last_login)}</TableCell>
                </TableRow>
              )) : null}
            </TableBody>


          </Table>
        </TableContainer>
      </Card>

      {modalHandlerChangeMaxUserStorage ? <Modal header="Success" closeModal={() => ModalHandlerChangeMaxUserStorage()} content={
        <div>
          <p>You changed the maximum storage capacity!</p>
          <button className="fileOption-button" onClick={() => ModalHandlerChangeMaxUserStorage()}>Close</button>
        </div>
      }></Modal> : null}

      {modalHandlerChangeLogoutTime == true ? <Modal header="Success" closeModal={() => ModalHandlerChangeLogoutTime()} content={
        <div>
          <p>You changed the auto-logout timer!</p>
          <button className="fileOption-button" onClick={() => ModalHandlerChangeLogoutTime()}>Close</button>
        </div>
      }></Modal> : null}
    </div>
  );
};
export default AdminPanel;
