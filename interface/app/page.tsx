"use client";
import { useState, useRef, useEffect } from "react";
import "./chat.css";

export default function Home() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>(
    []
  );
  const [input, setInput] = useState("");
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const bottomRef = useRef<HTMLDivElement>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    const response = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({ message: input }),
      headers: { "Content-Type": "application/json" },
    });

    const data = await response.json();
    const assistantMessage = { role: "assistant", content: data.reply };

    setMessages((prev) => [...prev, assistantMessage]);
  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="main-layout">
      <div className="chat-container">
        <div className="chat-header">
          Research Agent
          {!sidebarOpen && (
            <button
              className="open-button"
              onClick={() => setSidebarOpen(true)}
            >
              ☰
            </button>
          )}
        </div>

        <div className="chat-messages">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`chat-bubble ${msg.role === "user" ? "user" : "assistant"}`}
            >
              {msg.content}
            </div>
          ))}
          <div ref={bottomRef} />
        </div>

        <form onSubmit={handleSubmit} className="chat-input-bar">
          <div className="chat-icon">⚡</div>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="chat-input"
          />
        </form>
      </div>
    </div>
  );
}
