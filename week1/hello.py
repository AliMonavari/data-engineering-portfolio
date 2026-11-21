transactions = [
    {"account": "A1", "amount": 100},
    {"account": "A2", "amount": 250},
    {"account": "A1", "amount": 50},
]

totals = {}
for t in transactions:
    totals[t["account"]] = totals.get(t["account"], 0) + t["amount"]

print(totals)