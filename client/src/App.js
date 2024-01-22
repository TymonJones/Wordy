// src/App.js
import React, { useState } from 'react';
import Login from './Login';
import axios from 'axios'

const App = () => {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    setLoggedIn(true);
  };

  const handleLogout = async () => {
    try {
      // Make a request to your Flask backend to logout
      await axios.get('http://localhost:5000/logout');
      setLoggedIn(false);
    } catch (error) {
      console.error('Error during logout:', error);
      // Handle error (show an error message, etc.)
    }
  };

  return (
    <div>
      <h1>Welcome to Wordle!</h1>
      {loggedIn ? (
        <div>
          <p>You are logged in.</p>
          <button onClick={handleLogout}>Logout</button>
          {/* Render other game components when logged in */}
        </div>
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
};

export default App;
