import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import Loader from "../utils/Loader";

function Upload({ clickSubmit, handleChange, isFormFilled }) {
  const navigate = useNavigate();
  const { isLoading, isSuccess } = useSelector((state) => state.upload);

  useEffect(() => {
    if (isSuccess) {
      navigate("/chat");
    }
  }, [isSuccess, navigate]);

  return (
    <>
      <div className="relative">
        <form>
          <label
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            htmlFor="large_size"
          >
            Large file input
          </label>
          <input
            onChange={handleChange("csv")}
            className="block m-auto text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            id="large_size"
            type="file"
          />
          {isFormFilled() ? (
            <button
              type="button"
              onClick={clickSubmit}
              className={`m-auto mt-2 block bg-blue-500 text-white font-bold py-2 px-4 rounded-full hover:bg-blue-700`}
            >
              Submit
            </button>
          ) : (
            <button
              type="button"
              disabled
              className={`m-auto mt-2 block bg-blue-500 text-white font-bold py-2 px-4 rounded-full opacity-50 cursor-not-allowed`}
            >
              Submit
            </button>
          )}
          {isLoading && (
            <>
              <Loader />
            </>
          )}
        </form>
      </div>
    </>
  );
}

export default Upload;
