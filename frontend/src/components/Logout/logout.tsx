import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const LogOut = ()=>{
   
    const navigate = useNavigate();

    useEffect(() => {
        //Implementing the setInterval method
        const interval = setInterval(() => {

            if(sessionStorage.getItem("login_datum") !== null){
                let loginDatumString = sessionStorage.getItem("login_datum")
                let loginDatum = new Date(parseInt(loginDatumString|| "0"))
                console.log(loginDatum)
                let loginEndeDatumString  = loginDatum.setMinutes(loginDatum.getMinutes() + 4)
                let loginEndeDatum = new Date(parseInt(loginEndeDatumString.toString()|| "0"))
                console.log(loginEndeDatum)

                if(loginEndeDatum < new Date()){
                    localStorage.removeItem("userID");
                    localStorage.removeItem("isAdmin");
                    sessionStorage.removeItem("login_datum");
                    navigate("/")
                }              
            }
        }, 10000);
        //Clearing the interval
        return () => clearInterval(interval);
    }, []);

    return <>
    
    </>
}

export default LogOut