# python imports
from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import traceback

# utils imports
from utils.logger import log_status
from utils.readable_timestamp import get_readable_timestamp
from utils.root_req_resp import RootRequestModel, RootResponseModel

# paths
constants_json_path = os.path.abspath("./constants.json")

# load .env and required keys
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Loading secrets from .env\n")
load_dotenv()
FASTAPI_ACCESS_KEY = os.getenv("FASTAPI_ACCESS_KEY")

# load constants.json
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Loading constants.json\n")
f_ptr = open(constants_json_path, "r", encoding="utf-8")
constants = json.load(f_ptr)
f_ptr.close()

# build FastAPI app
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Creating instance of FastAPI\n")
app = FastAPI(title=constants["FASTAPI_APP_TITLE"], version="0.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - for development
    # For production, use specific origins:
    # allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# root endpoint
@app.post("/", response_model=RootResponseModel)
def root():    #request: RootRequestModel):
    try:
        # endpoint hit; authenticate request
        log_status(status="INFO", source="/app.py::root()", timestamp=get_readable_timestamp(), msg="Root endpoint hit. Authenticating request\n")
        #if(request.fastapi_access_key != FASTAPI_ACCESS_KEY):
        #    log_status(status="WARNING", source="/app.py::root()", timestamp=get_readable_timestamp(), msg="FastAPI Access Key is either missing / mismatched. Authentication failed\n")
        #    # return response
        #    return RootResponseModel(
        #        response="401: Not Authorized"
        #    )
        ## return response
        #log_status(status="INFO", source="/app.py::root()", timestamp=get_readable_timestamp(), msg="Authentication successful. Returning response\n")
        return RootResponseModel(
            response="Its working, congrats!"
        )
    except Exception as e:
        log_status(status="ERROR", source="/app.py::root()", timestamp=get_readable_timestamp(), msg=f"Exception: {e}; traceback: {traceback.print_exc()}\n")

if __name__ == "__main__":
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)