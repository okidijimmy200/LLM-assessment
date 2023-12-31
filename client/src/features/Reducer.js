import { createSlice } from "@reduxjs/toolkit";
import { uploadFileSlice, chatSlice } from "./Slice";

export const upLoadFileReducer = createSlice({
  name: "upLoadFile",
  initialState: {
    result: "",
    isError: false,
    isSuccess: false,
    isLoading: false,
    message: "",
  },
  reducers: {
    reset: (state) => {
      state.isLoading = false;
      state.isError = false;
      state.isSuccess = false;
      state.message = "";
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(uploadFileSlice.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(uploadFileSlice.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.result = action.payload;
      })
      .addCase(uploadFileSlice.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      });
  },
});

export const chatReducer = createSlice({
  name: "chat",
  initialState: {
    result: "",
    isError: false,
    isSuccess: false,
    isLoading: false,
    message: "",
  },
  reducers: {
    reset: (state) => {
      state.isLoading = false;
      state.isError = false;
      state.isSuccess = false;
      state.message = "";
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(chatSlice.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(chatSlice.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.result = action.payload;
      })
      .addCase(chatSlice.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      });
  },
});
