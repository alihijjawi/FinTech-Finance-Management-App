import React from 'react';
import { useState } from "react";
import "../static/css/signin.css"
import logo from "../static/images/logo.jpg";

const SignIn = () => {
	return (
		<div>
				<meta charset="utf-8" />
				<meta
					name="viewport"
					content="width=device-width, initial-scale=1, shrink-to-fit=no"
				/>
				<link
					rel="stylesheet"
					href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css"
					integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
					crossorigin="anonymous"
				/>

				<title>Login | Fintech Game</title>
				<div class="wrapper">
					<div class="logo">
						<img
							src={logo}
							alt="LMAO"
						/>
					</div>
					<div class="text-center mt-4 name">~Fintech Game~</div>
					<form class="p-3 mt-3" action="/login" method="POST">
						<div class="form-field d-flex align-items-center">
							<span class="far fa-user"></span>
							<input
								type="text"
								name="userName"
								id="userName"
								placeholder="Username"
								autocomplete="off"
								required
							/>
						</div>
						<div class="form-field d-flex align-items-center">
							<span class="fas fa-key"></span>
							<input
								type="password"
								name="password"
								id="pwd"
								placeholder="Password"
								required
							/>
						</div>
						<button class="btn mt-3" type="submit">Login</button>
					</form>
					<div class="text-center fs-6">or <a href="/sign-up">Sign up</a></div>
					<br />
					<div class="text-center fs-6">
						<a href="/" class="button">BACK TO HOME</a>
					</div>
				</div>

				<script
					src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
					integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
					crossorigin="anonymous"
				></script>
				<script
					src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js"
					integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
					crossorigin="anonymous"
				></script>
				<script
					src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"
					integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
					crossorigin="anonymous"
				></script>
		</div>
	);
};

export default SignIn;
