"""Verkkosivun toimivuuden tarkistus."""
import time
from dataclasses import dataclass

import requests


@dataclass
class CheckResult:
    url: str
    ok: bool
    status_code: int | None = None
    response_time_ms: float | None = None
    error: str | None = None


def check_url(url: str, timeout: float = 5.0) -> CheckResult:
    """Tekee GET-pyynnön ja palauttaa tuloksen. Status < 400 tulkitaan OK:ksi."""
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException as exc:
        return CheckResult(url=url, ok=False, error=str(exc))
    elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
    return CheckResult(
        url=url,
        ok=response.status_code < 400,
        status_code=response.status_code,
        response_time_ms=elapsed_ms,
    )
