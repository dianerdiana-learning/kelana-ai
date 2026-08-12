def print_trip_summary(destination, country, days, budget, currency, travel_month):
    print("========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination  : {destination}")
    print(f"Country      : {country}")
    print(f"Days         : {days}")
    print(f"Budget       : {budget} {currency}")
    print(f"Currency     : {currency}")
    print(f"Travel Month : {travel_month}")


# Memanggil function dengan data spesifik
print_trip_summary(
    destination="Japan",
    country="Japan",
    days=5,
    budget=1500,
    currency="USD",
    travel_month="December",
)
