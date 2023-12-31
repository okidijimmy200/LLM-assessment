import React from "react";

function MessageBox({ message }) {
  return (
    <>
      <div className="max-w-xl p-4 mx-auto my-4 bg-blue-100 rounded-md whitespace-pre-wrap">
        <p className="text-gray-800">{message}</p>
      </div>
    </>
  );
}

export default MessageBox;
