"""
Relay Service: Connect to Nostr relays & publish an event
"""

import time
import logging
from typing import List

from nostr.key import PrivateKey
from nostr.event import Event
from nostr.relay_manager import RelayManager

logger = logging.getLogger(__name__)


class NostrRelayService:
    def __init__(self, private_key_hex: str, relays: List[str]):
        """
        Initialize the NostrRelayService with a private key and a list of relay URLs.

        :param private_key_hex: The bot's private key in hexadecimal format.
        :param relays: A list of relay WebSocket URLs.
        """
        if not self._is_valid_hex(private_key_hex):
            logger.error(
                "Invalid private key format. Must be a 64-character hexadecimal string."
            )
            raise ValueError("Invalid private key format.")

        self.private_key = PrivateKey(bytes.fromhex(private_key_hex))
        self.pubkey_hex = self.private_key.public_key.hex()
        self.pubkey_npub = self.private_key.public_key.bech32()

        self.relay_manager = RelayManager()
        for relay in relays:
            self.relay_manager.add_relay(relay)
        self.relay_manager.open_connections({"cert_reqs": 0})
        logger.info(f"Connected to relays: {relays}")
        time.sleep(1.5)

    def _is_valid_hex(self, s: str) -> bool:
        return len(s) == 64 and all(c in "0123456789abcdefABCDEF" for c in s)

    def publish_event(
        self, content: str = "", kind: int = 1, tags: List[List[str]] = []
    ) -> str:
        """
        Publish an event with the given content.

        :param content: The content to publish.
        :param kind: The kind of content being published (default: 1).
        :param tags: The tags for this event (default: None).
        :return: The ID of the published event.
        """
        event = Event(
            kind=kind,
            content=content,
            tags=tags,
            public_key=self.pubkey_hex,
        )
        self.private_key.sign_event(event)
        self.relay_manager.publish_event(event)
        logger.info(f"Published event: {content}, ID: {event.id}")
        return event.id

    def close(self):
        """
        Close all relay connections gracefully.
        """
        self.relay_manager.close_connections()
        logger.info("Closed relay connections.")
