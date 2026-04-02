# routes.py — All static data: routes, train types, travel classes

ROUTES: dict[tuple[str, str], int] = {
    ("New Delhi", "Mumbai"):    1460,
    ("New Delhi", "Kolkata"):   1525,
    ("New Delhi", "Chennai"):   2200,
    ("New Delhi", "Hyderabad"): 1670,
    ("Mumbai",    "Kolkata"):   1970,
    ("Mumbai",    "Chennai"):   1300,
    ("Mumbai",    "Hyderabad"):  711,
    ("Kolkata",   "Chennai"):   1200,
    ("Kolkata",   "Hyderabad"): 1600,
    ("Chennai",   "Hyderabad"):  633,
}


def get_distance(origin: str, destination: str) -> int | None:
    """Return distance in km between two cities (bidirectional)."""
    key = (origin, destination)
    reverse_key = (destination, origin)
    return ROUTES.get(key) or ROUTES.get(reverse_key)


# Train types: name -> (speed_kmph, fare_multiplier, surcharge_inr)
TRAIN_TYPES: dict[str, tuple[int, float, int]] = {
    "Fast Passenger": (90,  1.00,   0),
    "Express":        (110, 1.25,  50),
    "Superfast":      (120, 1.50, 100),
}

# Travel classes: name -> (fare_multiplier, baggage_allowance_kg)
TRAVEL_CLASSES: dict[str, tuple[float, int]] = {
    "Sleeper":    (1.0, 20),
    "AC 3-Tier":  (1.5, 30),
    "AC 2-Tier":  (2.0, 40),
}

CITIES: list[str] = sorted(set(
    city for pair in ROUTES for city in pair
))

PROMO_CODES: dict[str, object] = {
    "ADG20":     ("percent", 20),
    "WINTER500": ("flat",   500),
}
