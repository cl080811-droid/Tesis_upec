"""Registro temporal de ocupación del corral o comedero."""

from datetime import datetime


def create_record(count: int) -> dict:
    return {
        "timestamp": datetime.now().isoformat(),
        "cattle_count": int(count),
    }
