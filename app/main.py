import uvicorn as uvicorn
from fastapi import FastAPI

import app.api.router


#app = FastAPI()

#@app.get("/")
#def read_root():
    #return {"Hello": "World"}


def main() -> None:
    """Entrypoint of the application."""
    #set_multiproc_dir()
    uvicorn.run(
        "app.api.application:get_app",
        host="0.0.0.0",
        port=8000
    )

if __name__ == "__main__":
    main()