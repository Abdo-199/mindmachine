import { Card } from "@mui/material";
import CardContent from "@mui/material/CardContent";

import "../../styles/SearchResult/SearchResult.css";

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import BasicPie from "./PieChart";




function createData(
  Users: string,
  Email: number,
  Storage_usage: number,
  Last_access: number,
  Status: number,
) {
  return { Users, Email, Storage_usage, Last_access, Status };
}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
  createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
  createData('Eclair', 262, 16.0, 24, 6.0),
  createData('Cupcake', 305, 3.7, 67, 4.3),
  createData('Gingerbread', 356, 16.0, 49, 3.9),
];



const AdminPanel = () => {
  return (
    <div>
      <h4 style={{marginLeft:'20px' , textAlign:'center'}}>Statistics</h4>
      <Card style={{marginLeft:'200px', marginRight:'300px', minWidth:'500px' }} > 
          <CardContent>
            <BasicPie></BasicPie>
            <h4>test</h4>
          </CardContent>
      </Card>
      <h4 style={{marginLeft:'20px' , textAlign:'center'}}>Audio Logout</h4>
      <Card style={{marginLeft:'200px', marginRight:'300px', minWidth:'500px' }} > test</Card>
      <h4 style={{marginLeft:'20px' , textAlign:'center'}}>Statistics</h4>
      <Card style={{marginLeft:'200px', marginRight:'300px', minWidth:'500px' }} > test</Card>

      <TableContainer component={Paper}>
      <Table style={{marginLeft:'100px', marginRight:'300px', minWidth:'500px' }}  aria-label="simple table">
        <TableHead>
          <TableRow style={{minWidth:'50px', maxWidth:'150px'}}>
            <TableCell style={{minWidth:'50px', maxWidth:'150px'}}>Users</TableCell>
            <TableCell align="right">Email</TableCell>
            <TableCell align="right">User storage</TableCell>
            <TableCell align="right">Last access</TableCell>
            <TableCell align="right">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.Users}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.Users}
              </TableCell>
              <TableCell style={{minWidth:'50px', maxWidth:'150px'}} align="right">{row.Email}</TableCell>
              <TableCell align="right">{row.Storage_usage}</TableCell>
              <TableCell align="right">{row.Last_access}</TableCell>
              <TableCell align="right">{row.Status}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>





    </div>
  );
};
export default AdminPanel;
