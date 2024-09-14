from fastapi.responses import RedirectResponse
import uvicorn
from .models import Base
from .database import engine
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware


def main() -> None:
    app = FastAPI(
        title="Backend-Centung",
        description="Backend for Centung",
        version="1.0.0",
    )

    Base.metadata.create_all(bind=engine)

    @app.get("/")
    async def root(request: Request):
        return RedirectResponse("/docs", status_code=status.HTTP_302_FOUND)

    origins = [
        "http://194.238.16.213:4000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    print("Starting server...")
    uvicorn.run(app, host="localhost", port=4000)


if __name__ == "__main__":
    main()
