import axios from "axios";

const API_URL = "http://localhost:8000";

const uploadFile = async (fileData) => {
  const headers = {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  };

  const response = await axios.post(
    `${API_URL}/api/vi/document/upload-csv`,
    fileData,
    headers,
  );
  return response.data;
};

const chat = async (query) => {
  const headers = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await axios.post(
    `${API_URL}/api/vi/document/query-document`,
    query,
    headers,
  );
  return response.data;
};

const Service = {
  uploadFile,
  chat,
};
export default Service;
