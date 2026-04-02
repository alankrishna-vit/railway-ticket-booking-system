# fare.py — Pure math functions for the 6-step fare calculation

from routes import TRAIN_TYPES, TRAVEL_CLASSES


def calculate_slab_fare(distance_km: int) -> float:
    """Step 1: Base flat fee + distance slabs."""
    fare = 100.0  # flat base

    if distance_km <= 100:
        fare += distance_km * 1.00
    elif distance_km <= 300:
        fare += 100 * 1.00 + (distance_km - 100) * 0.80
    else:
        fare += 100 * 1.00 + 200 * 0.80 + (distance_km - 300) * 0.60

    return fare


def apply_senior_discount(fare: float, age: int) -> float:
    """Step 2: 40% discount for passengers above 60."""
    if age > 60:
        return fare * 0.60
    return fare


def apply_train_premium(fare: float, train_type: str) -> float:
    """Step 3: Multiply by train-type premium."""
    _, multiplier, _ = TRAIN_TYPES[train_type]
    return fare * multiplier


def apply_class_premium(fare: float, travel_class: str) -> float:
    """Step 4: Multiply by class premium."""
    multiplier, _ = TRAVEL_CLASSES[travel_class]
    return fare * multiplier


def apply_baggage_charge(fare: float, baggage_kg: float, travel_class: str) -> float:
    """Step 5: Add 15 INR per extra kg above class allowance."""
    _, allowance_kg = TRAVEL_CLASSES[travel_class]
    extra_kg = max(0.0, baggage_kg - allowance_kg)
    return fare + (extra_kg * 15)


def apply_surcharge(fare: float, train_type: str) -> float:
    """Step 6: Add flat surcharge based on train type."""
    _, _, surcharge = TRAIN_TYPES[train_type]
    return fare + surcharge


def calculate_passenger_fare(
    distance_km: int,
    age: int,
    baggage_kg: float,
    train_type: str,
    travel_class: str,
) -> float:
    """Run all 6 steps in order and return the final passenger fare."""
    fare = calculate_slab_fare(distance_km)        # Step 1
    fare = apply_senior_discount(fare, age)        # Step 2
    fare = apply_train_premium(fare, train_type)   # Step 3
    fare = apply_class_premium(fare, travel_class)  # Step 4
    fare = apply_baggage_charge(fare, baggage_kg, travel_class)  # Step 5
    fare = apply_surcharge(fare, train_type)       # Step 6
    return round(fare, 2)


def calculate_travel_time(distance_km: int, train_type: str) -> str:
    """Return estimated travel time as a human-readable string."""
    speed_kmph, _, _ = TRAIN_TYPES[train_type]
    total_minutes = round((distance_km / speed_kmph) * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}h {minutes}m"
