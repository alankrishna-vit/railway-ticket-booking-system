# Railway Ticket Booking System

A modular command-line railway ticket booking system in Python.

## Requirements
- Python 3.10 or higher (uses `int | None` union type hint syntax)

## How to run

1. Make sure all three files are in the same folder:
   - `routes.py`
   - `fare.py`
   - `main.py`
   - `README.md`

2. Open a terminal in that folder.

3. Run:
```
python main.py
```

## File overview

| File | Purpose |
|------|---------|
| `routes.py` | Static data — distances, train types, travel classes |
| `fare.py` | Pure math — 6-step fare calculation functions |
| `main.py` | Driver — user menus, input handling, final bill |

## Promo codes
- `ADG20` — 20% off the total
- `WINTER500` — ₹500 flat off (minimum total: ₹0)
```

---

## Step 4 — Running the program

Open the VS Code terminal (`Ctrl + `` ` ``) and type:
```
python main.py