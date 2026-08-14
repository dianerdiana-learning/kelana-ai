from services.trip_service import (
    calculate_daily_budget,
    get_trip_category,
    get_travel_season,
    get_recommended_transportation,
    get_recommended_places,
)


def print_recommended_places(places: list[str]):
    for place in places:
        print(f"- {place}")


def print_trip_summary(destination, country, days, budget, currency, travel_month):
    category = get_trip_category(budget)
    travel_season = get_travel_season(travel_month)
    daily_budget = calculate_daily_budget(budget, days)
    transportation = get_recommended_transportation(category)
    recommended_places = get_recommended_places(destination)

    print("========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination     : {destination}")
    print(f"Country         : {country}")
    print(f"Days            : {days}")
    print(f"Budget          : {budget:g} {currency}")
    print(f"Currency        : {currency}")
    print(f"Travel Month    : {travel_month}")
    print(f"Category        : {category}")
    print(f"Daily Budget    : {daily_budget:g} {currency}/Day")
    print(f"Season          : {travel_season}")
    print(f"Transportation  : {transportation}")
    print("\n")

    print("Recommended Places")
    print_recommended_places(recommended_places)


# Blok utama untuk menjalankan interaksi input
if __name__ == "__main__":
    print("--- Form Pengisian KelanaAI ---")

    # a. Input Interaktif beserta konversi tipe data
    destination = input("Masukkan Destination : ")
    country = input("Masukkan Country     : ")
    days = int(input("Masukkan Days        : "))
    budget = float(input("Masukkan Budget      : "))
    currency = input("Masukkan Currency    : ")
    travel_month = input("Masukkan Travel Month: ")

    print("\n")  # Memberikan jarak sebelum output hasil

    # b. Memanggil fungsi
    print_trip_summary(destination, country, days, budget, currency, travel_month)
