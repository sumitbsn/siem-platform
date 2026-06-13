import json
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler

app = FastAPI(title="Security Event Simulator API")

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(SlowAPIMiddleware)

with open("events.json") as f:
    EVENTS = json.load(f)


@app.get("/")
def home():
    return {
        "service": "SIEM Security Event Simulator",
        "status": "running",
        "available_endpoints": {
            "all_events": "/events",
            "authentication_events": "/api/auth",
            "firewall_events": "/api/firewall",
            "edr_events": "/api/edr",
            "cloud_events": "/api/cloud"
        },
        "total_events": len(EVENTS)
    }


def paginate(events, offset, limit):
    return {
        "offset": offset,
        "limit": limit,
        "total": len(events),
        "events": events[offset:offset+limit]
    }


@app.get("/events")
@limiter.limit("10/minute")
def get_events(
    request: Request,
    offset: int = 0,
    limit: int = 100
):
    return paginate(EVENTS, offset, limit)


@app.get("/api/auth")
@limiter.limit("10/minute")
def auth_events(
    request: Request,
    offset: int = 0,
    limit: int = 100
):

    auth_types = [
        "login_success",
        "login_failed",
        "vpn_login"
    ]

    filtered = [
        e for e in EVENTS
        if e["event_type"] in auth_types
    ]

    return paginate(filtered, offset, limit)


@app.get("/api/firewall")
@limiter.limit("10/minute")
def firewall_events(
    request: Request,
    offset: int = 0,
    limit: int = 100
):

    firewall_types = [
        "firewall_allow",
        "firewall_deny",
        "port_scan"
    ]

    filtered = [
        e for e in EVENTS
        if e["event_type"] in firewall_types
    ]

    return paginate(filtered, offset, limit)


@app.get("/api/edr")
@limiter.limit("10/minute")
def edr_events(
    request: Request,
    offset: int = 0,
    limit: int = 100
):

    filtered = [
        e for e in EVENTS
        if e["event_type"] == "process_start"
    ]

    return paginate(filtered, offset, limit)


@app.get("/api/cloud")
@limiter.limit("10/minute")
def cloud_events(
    request: Request,
    offset: int = 0,
    limit: int = 100
):

    filtered = [
        e for e in EVENTS
        if e["event_type"] == "vpn_login"
    ]

    return paginate(filtered, offset, limit)
