import React, { useState } from 'react';
import './App.css'; // Make sure to create and import a CSS file for styling

const App = () => {
  const [userInput, setUserInput] = useState('');
  const [inputHistory, setInputHistory] = useState([]);

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      setInputHistory([...inputHistory, userInput]);
      setUserInput('');
    }
  };

  return (
    <div className="container">
      <div className="box image-box">
        {/* Image will be placed here */}
      </div>
      <div className="box text-box">
        <h1>Your Story Starts Now</h1>
      </div>
      <div className="box input-box">
        <div
          contentEditable
          className="terminal-input"
          onInput={(e) => setUserInput(e.currentTarget.textContent)}
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              e.preventDefault();
              setInputHistory([...inputHistory, userInput]);
              setUserInput('');
              e.currentTarget.textContent = '';
            }
          }}
        ></div>
      </div>
    </div>
  );
};

export default App;