"""
Set Bot Profile
"""

#!/usr/bin/env python3

import json

from fiatjafbuzz.logging import logging
from fiatjafbuzz.relay_service import NostrRelayService
from fiatjafbuzz.settings import Settings

logger = logging.getLogger(__name__)


def main():
    settings = Settings()
    profile_content = {
        "display_name": settings.profile_display_name,
        "about": settings.profile_about,
        "picture": settings.profile_display_pic_url,
    }

    relay_service = NostrRelayService(
        private_key_hex=settings.private_key_hex, relays=settings.relays_list
    )

    try:
        event_id = relay_service.publish_event(
            kind=0,
            content=json.dumps(profile_content),
        )
        logger.info(f"Successfully published profile event with ID: {event_id}")
        logger.info(f"Public key (npub): {relay_service.pubkey_npub}")
    except Exception as e:
        logger.error(f"Error publishing profile event: {e}")
    finally:
        relay_service.close()

    relay_service.close()
