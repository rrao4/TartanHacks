import React, { useState, useEffect } from 'react';
import './App.css';
import Animation from './Animation';

const App = () => {
  const [userInput, setUserInput] = useState('');
  const [displayedText, setDisplayedText] = useState('');
  const [loading, setLoading] = useState(false); // loading state for animation
  const [showWelcome, setShowWelcome] = useState(true); // welcome screen state

  useEffect(() => {
    // Start a new game when the app loads
    fetch('http://127.0.0.1:5000/start', { method: 'POST' })
      .then((res) => res.json())
      .then(() => setDisplayedText("A new adventure begins. Type any theme you would like to play."))
      .catch((err) => console.error("Failed to start game:", err));
  }, []);

  const handleKeyPress = async (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      if (!userInput.trim()) return; // prevent empty input

      setLoading(true); // start running animation

      const userText = `> ${userInput}`;
      setDisplayedText(userText); // replace displayed text with user input
      setUserInput('');
      e.currentTarget.textContent = ''; // clear user input

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
          setDisplayedText(`${data.story_beat}`); // replace text with AI response

          // If beat_count is 8, reset the story
          if (data.state.beat_count === 0) {
            setTimeout(() => setDisplayedText("--- A New Story Begins ---"), 2000);
          }
        }
      } catch (error) {
        console.error('Error communicating with API:', error);
        setDisplayedText(`[Error] Failed to reach the server.`);
      } finally {
        setLoading(false); // back to standing animation
      }
    }
  };

  const handleStartClick = () => {
    setShowWelcome(false); // hide welcome screen
  };

  return (
    <div className="container">
      {showWelcome ? (
        <div className="welcome-screen">
          <h1>Welcome to Your Adventure</h1>
          <button onClick={handleStartClick}>Start</button>
        </div>
      ) : (
        <>
          <div className="box image-box">
            <Animation isRunning={loading} /> {/* Pass loading state */}
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
        </>
      )}
    </div>
  );
};

export default App;
