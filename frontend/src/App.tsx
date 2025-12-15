import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

interface Message {
  id: number;
  text: string;
  fromMe: boolean;
  timestamp: string;
}

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchMessages();
  }, []);

  const fetchMessages = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/messages`);
      console.log("MESSAGES FROM API", response.data);
      setMessages(response.data);
    } catch (error) {
      console.error('Error fetching messages:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!inputValue.trim()) return;

    try {
      const response = await axios.post(`${API_URL}/messages`, {
        text: inputValue,
        fromMe: true
      });
      setMessages([...messages, response.data]);
      setInputValue('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="app">
      <div className="chat-container">
        <header className="chat-header">
          <h1>Chat</h1>
          <p>Friend</p>
        </header>
        
        <main className="messages-area">
          {loading ? (
            <div className="loading">Loading messages...</div>
          ) : messages.length === 0 ? (
            <div className="empty-state">No messages yet. Start a conversation!</div>
          ) : (
            messages.map((msg) => (
              <div key={msg.id} className={`message ${msg.fromMe ? 'from-me' : 'from-other'}`}>
                <div className="message-content">
                  <p>{msg.text}</p>
                </div>
                <span className="message-time">
                  {new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </span>
              </div>
            ))
          )}
        </main>
        
        <form onSubmit={handleSendMessage} className="input-form">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Type a message..."
            className="message-input"
          />
          <button type="submit" className="send-btn">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
