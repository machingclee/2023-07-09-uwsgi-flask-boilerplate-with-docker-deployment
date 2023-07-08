import os

from flask import Flask
from src.controllers.script_controller import script_controller
from dotenv import load_dotenv
import sys

src_dir = os.path.dirname(__file__)
if src_dir not in  sys.path:
    sys.path.append(src_dir)

app = Flask(__name__)
app.register_blueprint(script_controller)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    conf_env_path = os.path.sep.join([src_dir, "config.env"])
    load_dotenv(dotenv_path=conf_env_path)
    PORT = os.getenv("PORT")
    print(f"Running application in port {PORT}")
    app.run(port=PORT)
