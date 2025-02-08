import React, { useState, useEffect } from 'react';
import './App.css'; // Ensure this file exists for styling

const App = () => {
  const [userInput, setUserInput] = useState('');
  const [displayedText, setDisplayedText] = useState(''); // Only show the latest response
  const [loading, setLoading] = useState(false); // Loading state while waiting for AI response

  useEffect(() => {
    // Start a new game when the app loads
    fetch('http://127.0.0.1:5000/start', { method: 'POST' })
      .then((res) => res.json())
      .then(() => setDisplayedText("--- A New Story Begins ---")) // Show reset message
      .catch((err) => console.error("Failed to start game:", err));
  }, []);

  const handleKeyPress = async (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      if (!userInput.trim()) return; // Prevent empty input

      setLoading(true); // Show loading state

      const userText = `> ${userInput}`;
      setDisplayedText(userText); // Replace displayed text with user input
      setUserInput('');
      e.currentTarget.textContent = ''; // Clear input field

      try {
        const response = await fetch('http://127.0.0.1:5000/nextBeat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ user_input: userInput }),
        });

        const data = await response.json();

        if (data.error) {
          console.error('API Error:', data.error);
          setDisplayedText(`[Error] ${data.error}`);
        } else {
          setDisplayedText(`${data.story_beat}`); // Replace text with AI response

          // If beat_count is 10, reset the story
          if (data.state.beat_count === 0) {
            setTimeout(() => setDisplayedText("--- A New Story Begins ---"), 2000);
          }
        }
      } catch (error) {
        console.error('Error communicating with API:', error);
        setDisplayedText(`[Error] Failed to reach the server.`);
      } finally {
        setLoading(false);
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
          <p>{displayedText}</p> {/* Only show the latest response */}
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
