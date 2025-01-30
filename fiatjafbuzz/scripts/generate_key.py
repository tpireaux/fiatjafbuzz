"""
Generate Keys for the Bot!
"""

#!/usr/bin/env python3

from nostr.key import PrivateKey


def main():
    pk = PrivateKey()
    print(f"private key: {pk.hex()}")
    print(f"public key: {pk.public_key.bech32()}")
