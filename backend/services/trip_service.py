def calculate_daily_budget(budget: float, days: int):
    return budget / days


def get_trip_category(budget: float):
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"


def get_travel_season(month: str):
    lowered_month = month.lower()

    if lowered_month == "december":
        return "Peak Season"
    elif lowered_month == "june":
        return "Holiday Season"
    else:
        return "Regular Season"


def get_recommended_transportation(category: str):
    lowered_category = category.lower()

    if lowered_category == "backpacker":
        return "Bus"
    elif lowered_category == "standard":
        return "Train"
    else:
        return "Flight"


def get_recommended_places(destination: str):
    place_recommendations = {
        "japan": ["Tokyo Tower", "Shibuya", "Mount Fuji"],
        "bali": ["Ubud", "Kuta Beach", "Tanah Lot"],
        "singapore": ["Marina Bay Sands", "Gardens by the Bay", "Sentosa"],
    }

    return place_recommendations.get(
        destination.lower(), ["City Center", "Local Market", "Popular Landmark"]
    )
