import React from 'react';
import { Link } from "react-router-dom";

const Home = () => {
return (
	<div>
	<head>
    <title>Pre-Game Menu</title>
    <link
      href="{{ url_for('static', filename='css/index.css') }}"
      rel="stylesheet"
      type="text/css"
    />
  </head>

  <body>
    <div id="allthethings">
      <div id="left"></div>
      <div id="single">
        <Link to="/about"><p>PLAY</p></Link>
      </div>
      <div id="tutorial">
        <Link to="/about"><p>TUTORIAL</p></Link>
      </div>
      <div id="options">
	  	<Link to="/about"><p>OPTIONS</p></Link>
      </div>
      <div id="credits">
	  	<Link to="/about"><p>CREDITS</p></Link>
      </div>
      <div id="right"></div>
      <div id="top"></div>
      <div id="exit"></div>
      
      <div id="circle" class="circ">
      </div>
     
    </div>
  </body>
	</div>
);
};

export default Home;
