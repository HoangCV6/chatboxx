import { useState } from "react";

export default function AdminChat() {
  const [users] = useState([
    { id: 1, name: "User 1" },
    { id: 2, name: "User 2" }
  ]);

  const [selectedUser, setSelectedUser] = useState(null);

  return (
    <div className="flex h-screen bg-[#343541] text-white">
      
      {/* Sidebar user list */}
      <div className="w-64 bg-[#202123] p-4">
        <h2 className="mb-4">Users</h2>
        {users.map((u) => (
          <div
            key={u.id}
            className="p-2 hover:bg-gray-700 cursor-pointer"
            onClick={() => setSelectedUser(u)}
          >
            {u.name}
          </div>
        ))}
      </div>

      {/* Chat viewer */}
      <div className="flex-1 p-4">
        {selectedUser ? (
          <>
            <h2>Chat với {selectedUser.name}</h2>

            <div className="mt-4 bg-gray-800 p-4 rounded">
              (Hiển thị tin nhắn ở đây)
            </div>

            <div className="mt-4">
              <input
                className="w-full p-3 bg-gray-700 rounded"
                placeholder="Admin trả lời..."
              />
            </div>
          </>
        ) : (
          <div>Chọn user để xem chat</div>
        )}
      </div>
    </div>
  );
}