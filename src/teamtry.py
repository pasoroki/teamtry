import sys
import logging

from modules.parser import Parser
from modules.formatters.plaintext import Formatter_PlainText


time_pattern   = '%Y-%m-%d %H:%M:%S'
logging_format = "%(asctime)s [%(levelname)-8s] %(message)s"
logging_format = logging.Formatter(logging_format)
logging.basicConfig(stream=sys.stdout, format=logging_format, datefmt=time_pattern)
logger = logging.getLogger()

formatter = Formatter_PlainText()
parser = Parser(formatter)


def main():
    print("This is a main script")

    return parser.parse(data={1: "test"})


if __name__ == "__main__":
    exit(main())
