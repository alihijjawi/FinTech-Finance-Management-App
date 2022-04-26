import React from 'react';
import { Link } from "react-router-dom";
import "../static/css/index.css"

const Home = () => {
  return (
    <div>
      <title>Pre-Game Menu</title>
      <div id="allthethings">
        <div id="left"></div>
        <div id="single">
          <Link to="/sign-in"><p>PLAY</p></Link>
        </div>
        <div id="tutorial">
          <Link to="/about"><p>TUTORIAL</p></Link>
        </div>
        <div id="options">
          <Link to="/about"><p>OPTIONS</p></Link>
        </div>
        <div id="credits">
          <Link to="/blogs"><p>CREDITS</p></Link>
        </div>
        <div id="right"></div>
        <div id="top"></div>
        <div id="exit"></div>

        <div id="circle" className="circ">
        </div>

      </div>
    </div>
  );
};

export default Home;
