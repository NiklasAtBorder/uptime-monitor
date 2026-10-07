"""Ilmoitusten lähetys Discordiin."""
import requests

from monitor.checker import CheckResult


def build_message(result: CheckResult) -> str:
    if result.ok:
        return f"✅ {result.url} on taas ylhäällä ({result.response_time_ms} ms)"
    reason = result.error or f"HTTP {result.status_code}"
    return f"🔴 {result.url} ei vastaa: {reason}"


def send_discord(webhook_url: str, message: str) -> None:
    response = requests.post(webhook_url, json={"content": message}, timeout=5)
    response.raise_for_status()
