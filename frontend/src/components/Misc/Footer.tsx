import React from 'react'
import '../../styles/Misc/Footer.css'
import { useNavigate } from "react-router-dom";

const Footer = () => {

  const navigate = useNavigate();

  return (
    <div id="footer-container">Mind-Machine WebApp 2023 |  <span onClick={() => navigate("/LegalNotice")} id="legalNotice-link">Impressum</span></div>
  )
}

export default Footer