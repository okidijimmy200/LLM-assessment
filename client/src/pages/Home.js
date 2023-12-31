import React from "react";
import Uploads from "../containers/Uploads";

export default function Home() {
  return (
    <div className="">
            <div className="bg-gray-100 flex items-center justify-center h-screen">
        <div className="max-w-md p-6 bg-white rounded-lg shadow-md">
          <h1 className="text-2xl font-bold mb-4">Question & Answer Application</h1>
          <p className="text-gray-600 mb-6">
            Utilize our simple Question and Answer application powered by
            Language Model technology to effortlessly query uploaded documents.
          </p>
          <p className="text-gray-600 mb-6">
            Upload a CSV file and start querying today!
          </p>
          <div className="flex justify-start">
            <Uploads />
          </div>
        </div>
      </div>
      
    </div>
  );
}
