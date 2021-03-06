import React from 'react';
import { useState } from "react";
import "../static/css/signup.css"
import logo from "../static/images/logo.jpg";
import { saveUserToken, getUserToken, clearUserToken } from '../localStorage';

const SignUp = () => {
	let [username, setUsername] = useState("");
	let [pwdInput, setPwdInput] = useState("");
	let [confPwdInput, setConfPwdInput] = useState("");
	
	function verifyPassword() {
		if (pwdInput !== confPwdInput) {
			alert("Passwords do not match.");
		}
		else{
			singup()
		}
	}

	function singup() {
		var data = {
			"username": username,
			"pwd": pwdInput
		}
		console.log(username)
		return fetch(`http://localhost:5000/signup`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		}).then((response) => signIn());
	}

	function signIn(){
		var data = {
			"username": username,
			"pwd": pwdInput
		}
		return fetch(`http://localhost:5000/login`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		})
			.then(response => response.json())
			.then((body) => {
				saveUserToken(body.token)
			});
	}
	
	return (
		<div>
			<meta charSet="utf-8" />
			<meta
				name="viewport"
				content="width=device-width, initial-scale=1, shrink-to-fit=no"
			/>

			<link
				rel="stylesheet"
				href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css"
				integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
				crossOrigin="anonymous"
			/>

			<title>Register | Fintech Game</title>

			<div className="wrapper">
				<div className="logo">
					<img src={logo} alt="LMAO"/>
				</div>
				<div className="text-center mt-4 name">~Fintech Game~</div>
				<form>
					<div className="form-field d-flex align-items-center">
						<span className="far fa-user"></span>
						<input
							type="text"
							name="userName"
							id="userName"
							placeholder="Username"
							autoComplete="off"
							value={username}
							onChange={({ target: { value } }) => setUsername(value)}
							required
						/>
					</div>
					<div className="form-field d-flex align-items-center">
						<span className="fas fa-key"></span>
						<input
							type="password"
							name="password"
							id="pwd"
							placeholder="Password"
							value={pwdInput}
							onChange={({ target: { value } }) => setPwdInput(value)}
							required
						/>
					</div>
					<div className="form-field d-flex align-items-center">
						<span className="fas fa-key"></span>
						<input
							type="password"
							name="confirmpassword"
							id="confpwd"
							value={confPwdInput}
							onChange={({ target: { value } }) => setConfPwdInput(value)}
							placeholder="Confirm Password"
							required
						/>
					</div>
				</form>
				<button className="btn mt-3" onClick={verifyPassword}>Register</button>
				<div className="text-center fs-6">
					<a href="/">BACK TO HOME</a>
				</div>
			</div>

			<script
				src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
				integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
				crossOrigin="anonymous"
			></script>
			<script
				src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js"
				integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
				crossOrigin="anonymous"
			></script>
			<script
				src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"
				integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
				crossOrigin="anonymous"
			></script>

		</div>
	);
};

export default SignUp;
