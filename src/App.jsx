import React, { useState } from 'react';
import './App.css'; // Make sure you have a CSS file for styling

const App = () => {
  const [userInput, setUserInput] = useState('');
  const [inputHistory, setInputHistory] = useState([]);
  const [loading, setLoading] = useState(false); // Loading state while waiting for AI response

  const handleKeyPress = async (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      if (!userInput.trim()) return; // Prevent sending empty input

      setLoading(true); // Show loading state

      setUserInput('');
      e.currentTarget.textContent = ''; // Clear the contentEditable div

      try {
        const response = await fetch('http://127.0.0.1:5000/nextBeat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_input: userInput, // Send user input to backend
            state: {}, // Include game state if needed
          }),
        });

        const data = await response.json();

        if (data.error) {
          console.error('API Error:', data.error);
          setInputHistory([`[Error] ${data.error}`]);
        } else {
          setInputHistory([data.story_beat]);
        }
      } catch (error) {
        console.error('Error communicating with API:', error);
        setInputHistory([`[Error] Failed to reach the server.`]);
      } finally {
        setLoading(false); // Hide loading state
      }
    }
  };

  return (
    <div className="container">
      <div className="box image-box">
        {/* Image will be placed here */}
      </div>
      <div className="box text-box" id="middleBox">
        <div className="terminal-content">
          {inputHistory.map((line, index) => (
            <p key={index}>{line}</p>
          ))}
          {loading && <p>Story is playing out...</p>}
        </div>
      </div>
      <div className="box input-box">
        <div
          contentEditable
          className="terminal-input"
          onInput={(e) => setUserInput(e.currentTarget.textContent)}
          onKeyPress={handleKeyPress}
          autoFocus
        ></div>
      </div>
    </div>
  );
};

export default App;
