import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { chatSlice } from "../features/Slice";
import Query from "../components/Query";

function Querys() {
  const dispatch = useDispatch();

  const [values, setValues] = useState({
    question: "",
  });

  const handleChange = (name) => (event) => {
    setValues({ ...values, [name]: event.target.value });
  };
  const clickSubmit = (e) => {
    e.preventDefault();

    const Data = {
      query: values?.question,
    };

    dispatch(chatSlice(Data));
  };
  return (
    <>
      <Query
        clickSubmit={clickSubmit}
        handleChange={handleChange}
        values={values}
      />
    </>
  );
}

export default Querys;
