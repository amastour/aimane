import os
from app import create_app

app = create_app(os.getenv("CONFIG_TYPE") or "dev")
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)