// src/Login.js
import React, { useState } from 'react';
import axios from 'axios';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      // Make a request to your Flask backend for user authentication
      const response = await axios.post('http://localhost:5000/login', {
        username,
        password,
      });

      // If login is successful, invoke the onLogin callback
      if (response.data.success) {
        onLogin();
      } else {
        // Handle unsuccessful login (show an error message, etc.)
      }
    } catch (error) {
      console.error('Error during login:', error);
      // Handle error (show an error message, etc.)
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
