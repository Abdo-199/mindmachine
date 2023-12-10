import React ,{ useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const LogOutTimer = () => {
   
    const events = [
        "load",
        "mousemove",
        "mousedown",
        "click",
        "scroll",
        "keypress",
      ];

    const navigate = useNavigate();

    const [chrono, setChrono] = useState("")

    const  parseMillisecondsIntoReadableTime = (milliseconds : any) =>{
        //Get hours from milliseconds
        var hours = milliseconds / (1000*60*60);
        var absoluteHours = Math.floor(hours);
      
        //Get remainder from hours and convert to minutes
        var minutes = (hours - absoluteHours) * 60;
        var absoluteMinutes = Math.floor(minutes);
        var m = absoluteMinutes > 9 ? absoluteMinutes : '0' +  absoluteMinutes;
      
        //Get remainder from minutes and convert to seconds
        var seconds = (minutes - absoluteMinutes) * 60;
        var absoluteSeconds = Math.floor(seconds);
        var s = absoluteSeconds > 9 ? absoluteSeconds : '0' + absoluteSeconds;
    
        return  m + ':' + s;
    }

    useEffect(() => {

        //Reset the timer after any event
        Object.values(events).forEach((item) => {
            window.addEventListener(item, () => {
                sessionStorage.setItem("login_datum", new Date().getTime().toString())
            })
        })
        //Implementing the setInterval method
        const interval = setInterval(() => {

            if(sessionStorage.getItem("login_datum") !== null){
                let loginDatumString = sessionStorage.getItem("login_datum")
                let loginDatum = new Date(parseInt(loginDatumString|| "0"))
                console.log(loginDatum)
                let loginEndeDatumString  = loginDatum.setHours(loginDatum.getHours() + 1)
                let loginEndeDatum = new Date(parseInt(loginEndeDatumString.toString()|| "0"))
                console.log(loginEndeDatum)

                let aktuelleZeit = new Date()

                if(loginEndeDatum < aktuelleZeit){
                    localStorage.removeItem("userID")
                    localStorage.removeItem("isAdmin")
                    sessionStorage.removeItem("login_datum")
                    navigate("/")
                }  
                else {

                    //Calculate time difference
                    let differentInTime = loginEndeDatum.getTime() - aktuelleZeit.getTime()
                    let time = parseMillisecondsIntoReadableTime(differentInTime)
                    setChrono( time)
                }            
            } 
        }, 1000);
        //Clearing the interval
        return () => clearInterval(interval);
    }, [])

    return <span style={{color:"red", fontSize:20}}> {chrono}
    </span>
}

export default LogOutTimer