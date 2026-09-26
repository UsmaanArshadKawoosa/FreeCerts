#!/usr/bin/env python3
"""
FreeCerts Link Checker (Optional)

Checks certification URLs for accessibility.
Handles redirects, timeouts, and rate limits gracefully.
Does not mark certifications as paid or expired solely because a website is temporarily unavailable.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
import ssl
from typing import List, Dict, Any, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERTIFICATIONS_FILE = os.path.join(BASE_DIR, "data", "certifications.json")

TIMEOUT = 10  # seconds
RETRY_DELAY = 2  # seconds
MAX_RETRIES = 2


def check_url(url: str) -> Tuple[bool, str, int]:
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "FreeCerts-LinkChecker/1.0")

        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as response:
            return True, str(response.status), response.status

    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}", e.code
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}", 0
    except TimeoutError:
        return False, "Timeout", 0
    except Exception as e:
        return False, f"Error: {str(e)}", 0


def check_url_with_retry(url: str) -> Tuple[bool, str, int]:
    for attempt in range(MAX_RETRIES):
        success, message, code = check_url(url)
        if success:
            return success, message, code
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)
    return success, message, code


def main():
    if not os.path.exists(CERTIFICATIONS_FILE):
        print(f"ERROR: {CERTIFICATIONS_FILE} not found")
        sys.exit(1)

    with open(CERTIFICATIONS_FILE, "r", encoding="utf-8") as f:
        certifications = json.load(f)

    if not certifications:
        print("No certifications found")
        return

    print(f"Checking {len(certifications)} certification URLs...")
    print()

    results = []
    for cert in certifications:
        cert_id = cert.get("id", "unknown")
        url = cert.get("certification_url", "")
        name = cert.get("name", "Unknown")

        if not url:
            results.append((cert_id, name, url, False, "No URL provided", 0))
            continue

        success, message, code = check_url_with_retry(url)
        results.append((cert_id, name, url, success, message, code))

        status_symbol = "✓" if success else "✗"
        print(f"{status_symbol} [{cert_id}] {name[:50]}")
        print(f"    URL: {url}")
        print(f"    Status: {message}")
        print()

        time.sleep(0.5)

    accessible = sum(1 for r in results if r[3])
    total = len(results)

    print("=" * 50)
    print(f"Results: {accessible}/{total} URLs accessible")
    print("=" * 50)

    failed = [r for r in results if not r[3]]
    if failed:
        print("\nFailed URLs:")
        for cert_id, name, url, success, message, code in failed:
            print(f"  - [{cert_id}] {name}")
            print(f"    URL: {url}")
            print(f"    Reason: {message}")


if __name__ == "__main__":
    main()
