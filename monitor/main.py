"""Monitorin pääsilmukka. Käynnistys: python -m monitor.main [config.yaml]"""
import os
import sys
import time

import yaml

from monitor.checker import check_url
from monitor.notifier import build_message, send_discord


def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run(config_path: str = "config.yaml") -> None:
    config = load_config(config_path) # pyright: ignore[reportUnknownVariableType]
    interval = config.get("interval_seconds", 60)
    timeout = config.get("timeout_seconds", 5)
    webhook = os.environ.get("DISCORD_WEBHOOK_URL")
    state = {}  # url -> viimeisin ok-tila

    while True:
        for url in config["urls"]:
            result = check_url(url, timeout)
            previous = state.get(url)
            state[url] = result.ok
            print(f"[v5] {url} ok={result.ok} {result.response_time_ms} ms")

            # Ilmoitus vain kun tila muuttuu (tai ensimmäinen tarkistus epäonnistuu)
            changed = (not result.ok) if previous is None else previous != result.ok
            if changed and webhook:
                send_discord(webhook, build_message(result))
        time.sleep(interval)


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "config.yaml")
