# display.py — All terminal output: menus, prompts, and the final receipt

from routes import TRAIN_TYPES, TRAVEL_CLASSES


def print_header(title: str) -> None:
    print("\n" + "=" * 52)
    print(f"  {title}")
    print("=" * 52)


def print_welcome() -> None:
    print_header("RAILWAY TICKET BOOKING SYSTEM")
    print("  Welcome! Follow the steps below to book your ticket.")


def print_section(title: str) -> None:
    print(f"\n  ── {title} ──")


def show_route_confirmed(origin: str, destination: str, distance_km: int) -> None:
    print(
        f"\n  ✓ Route confirmed: {origin}  →  {destination}  ({distance_km} km)")


def show_passenger_header(num: int, total: int) -> None:
    print(f"\n  ── Passenger {num} of {total} ──")


def show_baggage_allowance(travel_class: str) -> None:
    _, allowance = TRAVEL_CLASSES[travel_class]
    print(f"  (Baggage allowance for {travel_class}: {allowance} kg)")


def show_subtotal(subtotal: float) -> None:
    print(f"\n  Subtotal (before promo): ₹{subtotal:.2f}")


def show_promo_result(label: str, is_valid: bool) -> None:
    if is_valid:
        print(f"  ✓ Promo applied: {label}")
    else:
        print("  ✗ Invalid promo code. Proceeding without discount.")


def build_train_menu() -> list[str]:
    """Return a list of display strings for the train type menu."""
    return [
        f"{name}  ({speed} km/h, ×{mult} fare, +₹{sur} surcharge)"
        for name, (speed, mult, sur) in TRAIN_TYPES.items()
    ]


def build_class_menu() -> list[str]:
    """Return a list of display strings for the travel class menu."""
    return [
        f"{name}  (×{mult} fare, {allow} kg baggage allowance)"
        for name, (mult, allow) in TRAVEL_CLASSES.items()
    ]


def print_booking_summary(
    origin: str,
    destination: str,
    distance_km: int,
    train_type: str,
    travel_class: str,
    travel_time: str,
    passengers: list[dict],
    promo_label: str,
    subtotal: float,
    final_total: float,
) -> None:
    print_header("BOOKING SUMMARY")
    print(f"  Route       : {origin}  →  {destination}")
    print(f"  Distance    : {distance_km} km")
    print(f"  Train       : {train_type}")
    print(f"  Class       : {travel_class}")
    print(f"  Travel time : ~{travel_time}")
    print()
    print(f"  {'Pax':<5} {'Age':<6} {'Baggage':>10} {'Senior':>8} {'Fare':>12}")
    print("  " + "-" * 46)
    for p in passengers:
        senior_tag = "Yes" if p["senior"] else "No"
        print(
            f"  {p['number']:<5} {p['age']:<6} "
            f"{p['baggage']:>8.1f} kg "
            f"{senior_tag:>8} "
            f"₹{p['fare']:>10.2f}"
        )
    print("  " + "-" * 46)
    print(f"  {'Subtotal':<32} ₹{subtotal:>10.2f}")
    if promo_label != "None":
        discount = subtotal - final_total
        print(f"  {'Discount (' + promo_label + ')':<32} ₹{discount:>10.2f}")
    print(f"  {'TOTAL PAYABLE':<32} ₹{final_total:>10.2f}")
    print("=" * 52)
    print("  Thank you for booking with Railway Ticket System!")
    print("=" * 52)
