import { useState } from 'react'
import './App.css'

function App() {
  const [userInput, setUserInput] = useState('')
  const [inputHistory, setInputHistory] = useState([])

  const handleInputChange = (e) => {
    setUserInput(e.target.value)
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      setInputHistory([...inputHistory, userInput])
      setUserInput('')
    }
  }

  return (
    <div className="terminal">
      <div
        contentEditable
        className="terminal-input"
        onInput={(e) => setUserInput(e.currentTarget.textContent)}
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            e.preventDefault()
            setInputHistory([...inputHistory, userInput])
            setUserInput('')
            e.currentTarget.textContent = ''
          }
        }}
        autoFocus
      />
      <div>
        {inputHistory.map((input, index) => (
          <p key={index}>{input}</p>
        ))}
      </div>
    </div>
  )
}

export default App