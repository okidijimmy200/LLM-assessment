import React from "react";
import { useSelector } from "react-redux";
import Loader from "../utils/Loader";
import Querys from "../containers/Querys";
import MessageBox from "../components/Message";
import LoadMessage from "../components/LoadMessage";

export default function Chat() {
  const { result, isLoading, isSuccess } = useSelector((state) => state.chat);
  return (
    <div className="">
      <Querys />
      {isLoading && <><Loader /> <LoadMessage/></>}
      {isSuccess && <MessageBox message={result.reason} />}
    </div>
  );
}
