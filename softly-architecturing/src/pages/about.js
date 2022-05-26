import React from "react";
import { Link } from "react-router-dom";
import "../static/css/homepage.css"
import stickman from "../static/images/stickman.png"

const About = () => {
	return (
		<>
		<div class="div">
			<p class="title">Homepage Title</p>
			<div id="single" class="left">
				<Link to="/account"><p class="text">ACCOUNT</p></Link>
			</div>
			<div id="tutorial" class="right">
				<Link to="/bank"><p class="text">BANK</p></Link>
			</div>
			<div id="options" class="bottomL">
				<Link to="/store"><p class="text">STORE</p></Link>
			</div>
			<div id="credits" class="bottomR">
				<Link to="/something"><p class="text">something</p></Link>
			</div>
		</div>
		<div class="user">
			<img class = "img" src={stickman} alt="user"/>
		</div>
		</>
	);
};

export default About;
