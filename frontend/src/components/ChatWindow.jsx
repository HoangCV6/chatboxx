export default function ChatWindow({ messages }) {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.map((msg, i) => (
        <div
          key={i}
          className={`p-3 rounded-lg max-w-xl ${
            msg.role === "user"
              ? "bg-green-600 self-end"
              : "bg-gray-700 self-start"
          }`}
        >
          {msg.content}
        </div>
      ))}
    </div>
  );
}