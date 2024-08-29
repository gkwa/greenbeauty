import argparse
import logging

from . import logger
from .anthropic_client import process_markdown_links
from .logging import configure_logging


def parse_arguments():
    parser = argparse.ArgumentParser(description="MyProject CLI")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase output verbosity (can be used multiple times)",
    )
    parser.add_argument(
        "-m",
        "--markdown-links",
        type=str,
        help="Path to file containing markdown links",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="response.md",
        help="Output file name (default: response.md)",
    )
    return parser.parse_args()


def process_markdown_file(input_file, output_file):
    with open(input_file, "r") as file:
        markdown_links = file.read()
    result = process_markdown_links(markdown_links)
    with open(output_file, "w") as file:
        for content_block in result:
            if content_block.type == "text":
                file.write(content_block.text)
    print(f"Response has been written to {output_file}")


def main():
    args = parse_arguments()
    configure_logging(args.verbose)

    if args.markdown_links:
        process_markdown_file(args.markdown_links, args.output)
    else:
        logger.info("Info level message")
        logger.debug("Debug level message")
        logger.log(logging.NOTSET, "Trace level message")
        print("Hello from greenbeauty!")


if __name__ == "__main__":
    main()
