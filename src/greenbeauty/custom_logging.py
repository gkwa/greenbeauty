import logging
import sys


def configure_logging(verbose_count):
    root = logging.getLogger()
    handler = logging.StreamHandler(sys.stderr)
    root.addHandler(handler)

    log_level = max(3 - verbose_count, 0) * 10
    root.setLevel(log_level)

    if verbose_count > 0:
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
    else:
        handler.setFormatter(logging.Formatter("%(message)s"))
