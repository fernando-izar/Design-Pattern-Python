from fastapi import FastAPI
from fastapi.responses import JSONResponse
from adapters.base import AppAdapter
from app.business_logic import get_hello
import uvicorn


class FastAPIAdapter(AppAdapter):
    def __init__(self):
        self.app = FastAPI()
        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/hello")
        def hello(name: str = "World"):
            return JSONResponse(get_hello(name))

        def run(self):
            uvicorn.run(self.app, host="127.0.0.1", port=8000)
