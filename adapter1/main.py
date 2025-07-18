import os
from adapters.flask_adapter import FlaskAdapter
from adapters.fastapi_adapter import FastAPIAdapter

if __name__ == "__main__":
    framework = os.getenv("FRAMEWORK", "flask").lower()

    adapter = FlaskAdapter() if framework == "flask" else FastAPIAdapter()
    adapter.run()
