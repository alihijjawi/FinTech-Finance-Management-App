import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './pages';
import About from './pages/about';
import Blogs from './pages/blogs';
import SignUp from './pages/signup';
import SignIn from './pages/signin';

function App() {
return (
	<Router>
	<Routes>
		<Route exact path='/' element={<Home/>}/>
		<Route path='/sign-in' element={<SignIn/>}/>
		<Route path='/about' element={<About/>}/>
		<Route path='/blogs' element={<Blogs/>}/>
		<Route path='/sign-up' element={<SignUp/>}/>
	</Routes>
	</Router>
);
}

export default App;
