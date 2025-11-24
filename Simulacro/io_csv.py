# io_csv.py
# CSV I/O utilities (Single Responsibility): only load/save CSV.
import csv
import os
from typing import Dict, List, Tuple

INV_HEADERS = ["id", "name", "brand", "category", "price", "stock", "warranty"]
SALE_HEADERS = ["date", "customer", "customer_type", "product_id", "product_name",
                "brand", "quantity", "unit_price", "gross_total", "discount_pct",
                "discount_amount", "net_total"]

def ensure_file(path: str, default_rows: List[List[str]]) -> None:
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(default_rows[0])
            for row in default_rows[1:]:
                writer.writerow(row)

def load_inventory_csv(path: str) -> Dict[int, dict]:
    data = {}
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f)):
            try:
                pid = int(row["id"]); price = float(row["price"])
                stock = int(row["stock"]); warranty = int(row["warranty"])
                data[pid] = {"name": row["name"], "brand": row["brand"],
                             "category": row["category"], "price": price,
                             "stock": stock, "warranty": warranty}
            except Exception:
                print(f"Skip invalid inventory row {i+1}")
    return data

def save_inventory_csv(path: str, inv: Dict[int, dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=INV_HEADERS)
        w.writeheader()
        for pid, p in sorted(inv.items()):
            w.writerow({"id": pid, "name": p["name"], "brand": p["brand"],
                        "category": p["category"], "price": p["price"],
                        "stock": p["stock"], "warranty": p["warranty"]})

def load_sales_csv(path: str) -> List[dict]:
    out = []
    if not os.path.exists(path):
        return out
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f)):
            try:
                out.append({
                    "date": row["date"], "customer": row["customer"],
                    "customer_type": row["customer_type"],
                    "product_id": int(row["product_id"]),
                    "product_name": row["product_name"], "brand": row["brand"],
                    "quantity": int(row["quantity"]),
                    "unit_price": float(row["unit_price"]),
                    "gross_total": float(row["gross_total"]),
                    "discount_pct": float(row["discount_pct"]),
                    "discount_amount": float(row["discount_amount"]),
                    "net_total": float(row["net_total"])
                })
            except Exception:
                print(f"Skip invalid sales row {i+1}")
    return out

def save_sales_csv(path: str, sales: List[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SALE_HEADERS)
        w.writeheader()
        for s in sales:
            w.writerow({k: s.get(k, "") for k in SALE_HEADERS})
