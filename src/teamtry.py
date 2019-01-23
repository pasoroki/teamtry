import sys
import logging


time_pattern   = '%Y-%m-%d %H:%M:%S'
logging_format = "%(asctime)s [%(levelname)-8s] %(message)s"
logging_format = logging.Formatter(logging_format)
logging.basicConfig(stream=sys.stdout, format=logging_format, datefmt=time_pattern)
logger = logging.getLogger()


def main():
    print("This is a main script")
    return 0


if __name__ == "__main__":
    exit(main())
