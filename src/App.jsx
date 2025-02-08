import { useState } from 'react'
import './App.css'

function App() {
  const [userInput, setUserInput] = useState('')
  const [inputHistory, setInputHistory] = useState([])

  const handleKeyPress = async (e) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      if (!userInput.trim()) return

      // Add user input to history
      const updatedHistory = [...inputHistory, `> ${userInput}`]
      setInputHistory(updatedHistory)
      setUserInput('')
      e.currentTarget.textContent = '' // Clear the input field

      try {
        const response = await fetch("http://127.0.0.1:5000/nextBeat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_input: userInput,
            state: {} // Add game state if needed
          })
        })

        const data = await response.json()
        if (data.error) {
          console.error("API Error:", data.error)
        } else {
          // Add AI response to history
          setInputHistory([...updatedHistory, `AI: ${data.story_beat}`])
        }
      } catch (error) {
        console.error("Error communicating with API:", error)
      }
    }
  }

  return (
    <div className="terminal">
      <div className="terminal-content">
        {inputHistory.map((line, index) => (
          <p key={index}>{line}</p>
        ))}
      </div>

      <div
        contentEditable
        className="terminal-input"
        onInput={(e) => setUserInput(e.currentTarget.textContent)}
        onKeyPress={handleKeyPress}
        autoFocus
      />
    </div>
  )
}

export default App
