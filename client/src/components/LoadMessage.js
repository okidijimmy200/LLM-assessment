import React from "react";

function LoadMessage() {
  return (
    <>
    <div className="relative">
    <div className="m-auto mt-2 max-w-md p-6 bg-white rounded-lg shadow-md">
        <h1 className="text-2xl font-bold mb-4">Querying document....</h1>
        <p className="text-gray-600 mb-6">This could take a minute, thanks for the patience.</p>
    </div>
    </div>

    </>
  );
}

export default LoadMessage;