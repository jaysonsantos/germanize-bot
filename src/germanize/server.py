from concurrent.futures import ThreadPoolExecutor

import flask
import telebot

from .bot import bot
from .constants import WEBHOOK_PATH

app = flask.Flask(__name__)

POOL = ThreadPoolExecutor()


@app.route("/")
def root():
    return "Hello world!"


@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") != "application/json":
        flask.abort(403)

    json_string = flask.request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    POOL.submit(bot.process_new_updates, [update])
    return ""


if __name__ == "__main__":
    print("Running app")
    app.run()
