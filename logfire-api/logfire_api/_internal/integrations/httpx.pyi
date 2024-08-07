from typing import Any

def instrument_httpx(**kwargs: Any):
    """Instrument the `httpx` module so that spans are automatically created for each request.

    See the `Logfire.instrument_httpx` method for details.
    """
