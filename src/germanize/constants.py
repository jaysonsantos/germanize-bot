import os
from urllib.parse import quote

BASE_URL = os.environ["BASE_URL"]
WEBHOOK_PATH = "/webhook/{}".format(quote(os.environ["SECRET"]))
WEBHOOK_URL = f"{BASE_URL}{WEBHOOK_PATH}"
