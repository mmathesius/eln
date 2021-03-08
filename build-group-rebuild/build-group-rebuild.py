#!/usr/bin/python3

import argparse
import json
import logging
import sys

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable debug logging",
        action="store_true",
    )

    message_group = parser.add_mutually_exclusive_group(required=True)

    message_group.add_argument(
        "-m",
        "--message",
        help="JSON contents of the *.koji-build-group.build.complete message",
        action="store",
        type=str,
    )

    message_group.add_argument(
        "-M",
        "--message-file",
        help="File containing JSON contents of the *.koji-build-group.build.complete message",
        action="store",
        type=str,
    )

    args = parser.parse_args()
    print("Args: {}".format(args))

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.message:
        msg_str = args.message
    else:
        if args.message_file == "-":
            msg_str = sys.stdin.read()
        else:
            with open(args.message_file, "r") as f:
                msg_str = f.read()

    logging.debug("Message as string: {}".format(msg_str))

    msg = json.loads(msg_str)

    logging.debug("Message as dict: {}".format(msg))
