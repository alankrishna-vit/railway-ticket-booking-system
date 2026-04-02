# main.py — Core orchestrator. Imports everything, does nothing else.

from routes import CITIES, TRAIN_TYPES, TRAVEL_CLASSES, PROMO_CODES, get_distance
from fare import calculate_passenger_fare, calculate_travel_time
from utils import get_int_input, get_float_input, get_optional_string, get_menu_choice
from display import (
    print_welcome, print_section,
    show_route_confirmed, show_passenger_header,
    show_baggage_allowance, show_subtotal, show_promo_result,
    build_train_menu, build_class_menu, print_booking_summary,
)


def select_route() -> tuple[str, str, int]:
    print_section("STEP 1: Choose your route")
    origin_idx = get_menu_choice(CITIES, "  → Origin city: ")
    origin = CITIES[origin_idx]

    destinations = [c for c in CITIES if c != origin]
    print()
    dest_idx = get_menu_choice(destinations, "  → Destination city: ")
    destination = destinations[dest_idx]

    distance = get_distance(origin, destination)
    if distance is None:
        print(f"\n  ✗ No direct route between {origin} and {destination}.")
        raise SystemExit(1)

    show_route_confirmed(origin, destination, distance)
    return origin, destination, distance


def select_train() -> str:
    print_section("STEP 2: Choose train type")
    idx = get_menu_choice(build_train_menu())
    return list(TRAIN_TYPES.keys())[idx]


def select_class() -> str:
    print_section("STEP 3: Choose travel class")
    idx = get_menu_choice(build_class_menu())
    return list(TRAVEL_CLASSES.keys())[idx]


def collect_passengers(
    num: int, distance: int, train_type: str, travel_class: str
) -> list[dict]:
    passengers = []
    for i in range(1, num + 1):
        show_passenger_header(i, num)
        age = get_int_input("  Age: ", 1, 120)
        show_baggage_allowance(travel_class)
        baggage = get_float_input("  Baggage weight (kg): ", min_val=0.1)
        fare = calculate_passenger_fare(
            distance, age, baggage, train_type, travel_class)
        passengers.append({
            "number": i, "age": age, "baggage": baggage,
            "senior": age > 60, "fare": fare,
        })
    return passengers


def apply_promo(subtotal: float) -> tuple[float, str]:
    code = get_optional_string(
        "\n  Enter promo code (or press Enter to skip): ").upper()
    if code == "":
        return subtotal, "None"
    if code not in PROMO_CODES:
        show_promo_result("", is_valid=False)
        return subtotal, "None"

    kind, value = PROMO_CODES[code]
    if kind == "percent":
        final = subtotal * (1 - value / 100)
        label = f"{code} (−{value}%)"
    else:
        final = max(0.0, subtotal - value)
        label = f"{code} (−₹{value})"

    show_promo_result(label, is_valid=True)
    return round(final, 2), label


def main() -> None:
    print_welcome()

    origin, destination, distance = select_route()
    train_type = select_train()
    travel_class = select_class()

    print_section("STEP 4: Passenger details")
    num_passengers = get_int_input("  Number of passengers (1–6): ", 1, 6)

    passengers = collect_passengers(
        num_passengers, distance, train_type, travel_class)

    subtotal = round(sum(p["fare"] for p in passengers), 2)
    show_subtotal(subtotal)

    final_total, promo_label = apply_promo(subtotal)
    travel_time = calculate_travel_time(distance, train_type)

    print_booking_summary(
        origin, destination, distance, train_type, travel_class,
        travel_time, passengers, promo_label, subtotal, final_total,
    )


if __name__ == "__main__":
    main()
