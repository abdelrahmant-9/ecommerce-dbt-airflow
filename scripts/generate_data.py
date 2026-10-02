"""Generate synthetic e-commerce CSVs into seeds/.

Deterministic (fixed random seed) so every run produces the same data.
Run: uv run python scripts/generate_data.py
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
SEEDS = Path(__file__).resolve().parent.parent / "seeds"

FIRST = ["Omar", "Sara", "Youssef", "Mona", "Karim", "Laila", "Ahmed", "Nour", "Hassan", "Salma",
         "Ali", "Farah", "Mostafa", "Hana", "Tamer", "Rana", "Khaled", "Dina", "Ziad", "Mariam"]
LAST = ["Hassan", "Ibrahim", "Mahmoud", "Saleh", "Fathy", "Nabil", "Adel", "Samir", "Tawfik", "Gamal"]
CITIES = ["Cairo", "Alexandria", "Giza", "Mansoura", "Tanta", "Aswan", "Luxor", "Port Said"]
PRODUCTS = [
    ("Wireless Mouse", "Electronics", 250), ("Mechanical Keyboard", "Electronics", 1450),
    ("USB-C Hub", "Electronics", 600), ("27in Monitor", "Electronics", 7200),
    ("Desk Lamp", "Home", 380), ("Office Chair", "Home", 4300), ("Standing Desk", "Home", 9800),
    ("Notebook A5", "Stationery", 45), ("Gel Pens (10)", "Stationery", 90),
    ("Backpack", "Accessories", 950), ("Water Bottle", "Accessories", 210),
    ("Noise-Cancelling Headphones", "Electronics", 5600),
]
STATUSES = ["completed"] * 8 + ["shipped", "cancelled", "returned"]


def write(name, header, rows):
    with open(SEEDS / f"{name}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"{name}.csv: {len(rows)} rows")


def main():
    SEEDS.mkdir(exist_ok=True)
    start = date(2025, 1, 1)

    customers = []
    for cid in range(1, 201):
        fn, ln = random.choice(FIRST), random.choice(LAST)
        email = f"{fn}.{ln}{cid}@example.com".lower()
        # ~3% messy emails to show cleaning in staging
        if random.random() < 0.03:
            email = "  " + email.upper() + " "
        customers.append([cid, fn, ln, email, random.choice(CITIES),
                          start - timedelta(days=random.randint(0, 700))])
    write("raw_customers", ["id", "first_name", "last_name", "email", "city", "signup_date"], customers)

    products = [[pid, n, c, p * 100] for pid, (n, c, p) in enumerate(PRODUCTS, 1)]  # price in cents
    write("raw_products", ["id", "name", "category", "price_cents"], products)

    orders, items = [], []
    item_id = 1
    for oid in range(1, 1501):
        orders.append([oid, random.randint(1, 200), start + timedelta(days=random.randint(0, 270)),
                       random.choice(STATUSES)])
        for _ in range(random.randint(1, 4)):
            prod = random.choice(products)
            items.append([item_id, oid, prod[0], random.randint(1, 3), prod[3]])
            item_id += 1
    write("raw_orders", ["id", "customer_id", "order_date", "status"], orders)
    write("raw_order_items", ["id", "order_id", "product_id", "quantity", "unit_price_cents"], items)


if __name__ == "__main__":
    main()
