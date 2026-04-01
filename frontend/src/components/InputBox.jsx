import { useState } from "react";

export default function InputBox({ onSend }) {
  const [text, setText] = useState("");

  return (
    <div className="p-4 border-t border-gray-600">
      <div className="flex gap-2">
        <input
          className="flex-1 p-3 rounded bg-gray-800"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Nhập câu hỏi..."
        />
        <button
          className="bg-green-600 px-4 rounded"
          onClick={() => {
            onSend(text);
            setText("");
          }}
        >
          Gửi
        </button>
      </div>
    </div>
  );
}