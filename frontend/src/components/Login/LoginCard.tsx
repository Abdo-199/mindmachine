import "../../styles/Login/LoginStyles.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginCard = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();


  const Login = async (username: string, password: string) =>  {

    let bodyData = { username: username, password: password };
  
    let fetchData = {
      method: "POST",
      body: JSON.stringify(bodyData),
      headers: {
        "Content-Type": "application/json",
      },
    };
  
    const url = "http://localhost:8000/login";
    const response = await fetch(url, fetchData)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        if (!data.isAuthenticated) {
          alert("Error. Wrong Credentials");
        }
        else {
          localStorage.setItem("userID", username)
          localStorage.setItem("isAdmin", data.isAdmin)

          //Weiterleitung zu MainWindow
          navigate("/MainWindow")
        }
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  return (
    // Username input, password input, ... on a card
    <div className="loginContainer">
      <img
        id="login-pic"
        className="avatar"
        // put in a much cooler logo for our web-app maybe?
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9YZj5Mx_JuC9-pYmy9DLJD9gTMl-jvV5lRoUNti104l9fSOxRqyE40rMajuUD2JYDCy0&usqp=CAU"
        alt="avatar"
        width={100}
        height={100}
      />
      <h1>Login</h1>
      <label htmlFor="username">Username</label>
      <br></br>
      <input
        id="username"
        className="login-input"
        placeholder="type in username ..."
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      ></input>
      <br></br>
      <label htmlFor="password">Password</label>
      <br></br>
      <input
        className="login-input"
        id="password"
        placeholder="type in password ..."
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      ></input>
      <br></br>
      <br></br>
      <div>
        <button className="login-button" onClick={() => Login(username, password)}>Login</button>
      </div>
    </div>
    //
  );
};

export default LoginCard;
