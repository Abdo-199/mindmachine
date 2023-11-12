import React from 'react'
import "../../styles/SearchResult/SearchResult.css";
import Header from '../Misc/Header'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material';


const SearchResult = () => {
    return (

        <div style={{backgroundColor:'white'}}>
            <Header></Header>
            <div> 
        <Card style={{backgroundColor:'#666BA9', marginTop:'20px'}} sx={{ maxWidth: 545 }}>
        
        <CardContent >
        <Typography style={{backgroundColor:'white'}} suppressContentEditableWarning={true} contentEditable={true} >
        
        
        
        
        </Typography>
        
        
        </CardContent>
        <CardActions>
        <Button size="small" style={{color :"black"}}>Open PDF</Button>
        <Button size="small" style={{color :"black" , marginRight:'20px'}}>Copy Result</Button>
        </CardActions>
        </Card>
            </div>
        </div>

    )
}
export default SearchResult