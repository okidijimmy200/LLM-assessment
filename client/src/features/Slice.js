import { createAsyncThunk } from "@reduxjs/toolkit";
import Service from "./Service";

export const uploadFileSlice = createAsyncThunk(
  "uploadFile",
  async (fileData, thunkAPI) => {
    try {
      return await Service.uploadFile(fileData);
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();
      return thunkAPI.rejectWithValue(message);
    }
  },
);

export const chatSlice = createAsyncThunk("chat", async (query, thunkAPI) => {
  try {
    return await Service.chat(query);
  } catch (error) {
    const message =
      (error.response && error.response.data && error.response.data.message) ||
      error.message ||
      error.toString();
    return thunkAPI.rejectWithValue(message);
  }
});
