import sys
import logging
import json
from os import environ


time_pattern   = '%Y-%m-%d %H:%M:%S'
logging_format = "%(asctime)s [%(levelname)-8s] %(message)s"
logging_format = logging.Formatter(logging_format)
logging.basicConfig(stream=sys.stdout, format=logging_format, datefmt=time_pattern)
logger = logging.getLogger()


async def processor(data):
    try:
        json_data = json.loads(data)
    except Exception as err:
        print(err)
        print(data)
        raise err
    result = {
        "title" : "New data arrived",
        "text"  : json.dumps(json_data, indent=4)
    }
    return result


from modules.web_server import WebServer
webserver = WebServer(port=environ.get("LISTEN_PORT", 8080))
webserver.register_webhook_for(
    webhook     = environ.get("URL_FRONTEND",   "/frontend"),
    destination = environ.get("TEAMS_FRONTEND", "http://localhost:8080/blah"),
    processor   = processor
)

def main():
    print("This is a main script")

    return webserver.run()


if __name__ == "__main__":
    exit(main())
