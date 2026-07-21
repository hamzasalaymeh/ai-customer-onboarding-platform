import { useState } from "react";
import { api } from "../api/client";
import type { ChatMessage } from "../types/customer";

export function ChatAssistant() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);

  async function sendMessage() {
    if (!input.trim()) return;
    const nextMessages: ChatMessage[] = [...messages, { role: "user", content: input }];
    setMessages(nextMessages);
    setInput("");
    setSending(true);
    try {
      const { reply } = await api.sendChatMessage(nextMessages);
      setMessages([...nextMessages, { role: "assistant", content: reply }]);
    } finally {
      setSending(false);
    }
  }

  return (
    <section>
      <h2>Ask the onboarding assistant</h2>
      <ul>
        {messages.map((message, index) => (
          <li key={index}>
            <strong>{message.role === "user" ? "You" : "Assistant"}:</strong> {message.content}
          </li>
        ))}
      </ul>
      <input
        value={input}
        onChange={(event) => setInput(event.target.value)}
        onKeyDown={(event) => event.key === "Enter" && sendMessage()}
        placeholder="Ask a question about onboarding…"
      />
      <button onClick={sendMessage} disabled={sending}>
        Send
      </button>
    </section>
  );
}
