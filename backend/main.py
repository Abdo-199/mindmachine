from api import API
from fastapi.middleware.cors import CORSMiddleware
import logHandler

api = API()
app = api.app

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    pass
    
    

if __name__ == '__main__':
    logger = logHandler.LogHandler(name="main").get_logger()
    logger.info("Application invoked")
    logger.info("Starting FastAPI server")    
    # start uvicorn server to host the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    main()