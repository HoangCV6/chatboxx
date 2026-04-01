import { useState } from "react";
import ChatWindow from "../components/ChatWindow";
import Sidebar from "../components/Sidebar";
import InputBox from "../components/InputBox";
import api from "../services/api";

export default function UserChat() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (text) => {
    const newMsg = { role: "user", content: text };
    setMessages((prev) => [...prev, newMsg]);

    const res = await api.post("/chat", {
      user_id: 1,
      message: text
    });

    setMessages((prev) => [
      ...prev,
      { role: "bot", content: res.data.reply }
    ]);
  };

  return (
    <div className="flex h-screen bg-[#343541] text-white">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <ChatWindow messages={messages} />
        <InputBox onSend={sendMessage} />
      </div>
    </div>
  );
}