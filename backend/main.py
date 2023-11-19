from qdrant import QDrant
from api import API
from fastapi.middleware.cors import CORSMiddleware

db = QDrant()

api = API(db)
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
    # start uvicorn server to host the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    main()