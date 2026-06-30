PLAN_LIMITS = {
    "Free": {
        "allowed_modes": ["fast"],
        "daily_requests": 2,
        "requests_per_minute": 5,
    },
    "Pro": {
        "allowed_modes": [
            "fast",
            "balanced",
        ],
        "daily_requests": 5000,
        "requests_per_minute": 60,
    },
    "Enterprise": {
        "allowed_modes": [
            "fast",
            "balanced",
            "maximum",
        ],
        "daily_requests": None,
        "requests_per_minute": None,
    },
}