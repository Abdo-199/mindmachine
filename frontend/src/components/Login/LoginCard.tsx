import { resolveSoa } from "dns";
import "../../styles/Login/LoginStyles.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

//Login-Card in the middle of the screen
const LoginCard = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  // send login requst to backend and inform user of success or error
  const Login = async (username: string, password: string) => {

      return await fetch(
        `${process.env.REACT_APP_production_address}/auth/token`,
        {
          method: "POST",
          body: new URLSearchParams({
            grant_type: 'password',
            username: username,
            password: password,
            client_id: 'your-client-id',
            client_secret: 'your-client-secret',
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      )
      .then((response) => {
        if (response.status === 401) {
          alert("Error. Wrong Credentials");
        }
        else {
          return response.json();
        }
      })
      .then((data) => {
        //sets the userID globally
        localStorage.setItem("userID", username);
        localStorage.setItem("isAdmin", data.is_admin);
        localStorage.setItem("token", data.access_token)
        sessionStorage.setItem(
          "login_datum",
          new Date().getTime().toString()
        );

        // navigate to MainWindow
        navigate("/MainWindow");

      })
      .catch(function (error) {

      });
  };

  // let user login with enter key
  const FastLogin = (e: any) => {
    if (e.key === "Enter") {
      Login(username, password);
    }
  };

  return (
    <div className="loginContainer">
      <img
        id="login-pic"
        className="avatar"
        src="mindmachine_logo.png"
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
        onKeyDown={(e) => FastLogin(e)}
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
        onKeyDown={(e) => FastLogin(e)}
      ></input>
      <br></br>
      <br></br>
      <div>
        <button
          className="login-button"
          onClick={() => Login(username, password)}
        >
          Login
        </button>
      </div>
    </div>
    //
  );
};

export default LoginCard;