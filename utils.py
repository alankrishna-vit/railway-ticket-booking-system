# utils.py — Reusable, crash-proof input helpers

def get_int_input(prompt: str, min_val: int, max_val: int) -> int:
    """Keep asking until the user gives a valid integer in range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(
                f"  ✗ Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ✗ Invalid input. Please enter a whole number.")


def get_float_input(prompt: str, min_val: float = 0.1) -> float:
    """Keep asking until the user gives a valid float at or above min_val."""
    while True:
        try:
            value = float(input(prompt))
            if value >= min_val:
                return value
            print(f"  ✗ Value must be at least {min_val}. Try again.")
        except ValueError:
            print("  ✗ Invalid input. Please enter a number (e.g. 15.5).")


def get_optional_string(prompt: str) -> str:
    """Get a string input — empty string is allowed (e.g. skipping promo)."""
    return input(prompt).strip()


def get_menu_choice(options: list[str], prompt: str = "  → Your choice: ") -> int:
    """Display a numbered list and return the 0-based index of the chosen item."""
    for i, option in enumerate(options, start=1):
        print(f"  [{i}] {option}")
    choice = get_int_input(prompt, 1, len(options))
    return choice - 1
