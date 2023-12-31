Client Side for Question and Answer document

This application is intended to perform question and answer to segments_csv file.
The file is first uploaded, then if successful, the user is redirected to the chat page
where they query the uploaded document. The responses generated from the server side LLM
are latter displayed in a message chat box.

1./api/vi/document/upload-csv 
method: POST
params: {"csv": csv}
This api is used to upload csv file to the backend.

2. /api/vi/document/query-document
method: POST
params: {"query": query}
This api is used to perfom query operations and the response is placed in a message box.

Challenges:
Decison on which format to organize the UI flow of events

Improvements:
1. Improve the UI to be more elaborate
2. write unittests
3. In the chat, keep record of previous chat messages and not only the current message

