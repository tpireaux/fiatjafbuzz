"""
Run the Bot!
"""

#!/usr/bin/env python3

import argparse
import datetime
import time

from fiatjafbuzz.relay_service import NostrRelayService
from fiatjafbuzz.settings import Settings
from fiatjafbuzz.logging import logging

logger = logging.getLogger(__name__)


def main():
    settings = Settings()

    parser = argparse.ArgumentParser(description="Run the Bot!")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode to force a debug message.",
    )
    args, _ = parser.parse_known_args()
    debug = args.debug

    today = datetime.date.today()
    day_of_week = today.weekday()
    day_of_year = today.timetuple().tm_yday

    message = None

    if day_of_week in (5, 6):  # sat/sun
        message = "gfy fiatjaf"
    else:
        if day_of_year % 2 == 0:
            message = "GM fiatjaf"

    if debug:
        message = f"Debug triggered at: {time.time_ns()}"

    if not message:
        logger.info("No message to publish.")
        return

    relay_service = NostrRelayService(
        private_key_hex=settings.private_key_hex, relays=settings.relays_list
    )

    time.sleep(1.5)

    logger.info(f"Publishing event: {message}")

    relay_service.publish_event(content=message)

    logger.info(f"Published event: {message}")

    time.sleep(2)
    relay_service.close()
