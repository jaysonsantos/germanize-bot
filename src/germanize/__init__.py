import logging

logging.basicConfig(
    format='%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
)

logger = logging.getLogger("TeleBot")
logger.setLevel(logging.DEBUG)
