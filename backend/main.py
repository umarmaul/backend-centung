from fastapi.responses import RedirectResponse
import uvicorn
from .models import Base
from .database import engine
from .routers import account, device, log, profile
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware


def main() -> None:
    app = FastAPI(
        title="Backend-Centung",
        description="Backend for Centung",
        version="1.0.0",
    )

    Base.metadata.create_all(bind=engine)

    @app.get("/" , tags=["home"])
    async def docs(request: Request):
        return RedirectResponse("/docs", status_code=status.HTTP_302_FOUND)

    origins = [
        "http://145.223.117.210:5000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(account.router)
    app.include_router(device.router)
    app.include_router(log.router)
    app.include_router(profile.router)  

    print("Starting server...")
    uvicorn.run(app, host="localhost", port=5000)


if __name__ == "__main__":
    main()
