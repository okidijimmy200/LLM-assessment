import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { uploadFileSlice } from "../features/Slice";
import Upload from "../components/Upload";

function Uploads() {
  const dispatch = useDispatch();

  const [values, setValues] = useState({
    csv: "",
  });

  const handleChange = (name) => (event) => {
    setValues({ ...values, [name]: event.target.files[0] });
  };

  const clickSubmit = (e) => {
    e.preventDefault();

    const fileData = {
      csv: values?.csv,
    };

    dispatch(uploadFileSlice(fileData));
  };
  const isFormFilled = () => {
    return Object.values(values).every((value) => {
      if (value instanceof File) {
        return true;
      }
      return false;
    });
  };
  return (
    <>
      <Upload
        clickSubmit={clickSubmit}
        handleChange={handleChange}
        isFormFilled={isFormFilled}
      />
    </>
  );
}

export default Uploads;
