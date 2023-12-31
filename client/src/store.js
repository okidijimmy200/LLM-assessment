import { configureStore } from "@reduxjs/toolkit";
import { upLoadFileReducer, chatReducer } from "./features/Reducer";

export default configureStore({
  reducer: {
    upload: upLoadFileReducer.reducer,
    chat: chatReducer.reducer,
  },
});
