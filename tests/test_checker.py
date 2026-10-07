from unittest.mock import MagicMock, patch

import requests

from monitor.checker import CheckResult, check_url
from monitor.notifier import build_message


@patch("monitor.checker.requests.get")
def test_check_url_ok(mock_get):
    mock_get.return_value = MagicMock(status_code=200)
    result = check_url("https://example.com")
    assert result.ok is True
    assert result.status_code == 200
    assert result.response_time_ms is not None


@patch("monitor.checker.requests.get")
def test_check_url_server_error(mock_get):
    mock_get.return_value = MagicMock(status_code=500)
    result = check_url("https://example.com")
    assert result.ok is False
    assert result.status_code == 500


@patch("monitor.checker.requests.get")
def test_check_url_connection_error(mock_get):
    mock_get.side_effect = requests.ConnectionError("yhteys katkesi")
    result = check_url("https://example.com")
    assert result.ok is False
    assert result.status_code is None
    assert "yhteys katkesi" in result.error


def test_build_message_down():
    result = CheckResult(url="https://example.com", ok=False, status_code=503)
    assert "HTTP 503" in build_message(result)
