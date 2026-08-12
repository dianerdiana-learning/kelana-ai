def print_trip_summary(destination, country, days, budget, currency, travel_month):
    print("========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination  : {destination}")
    print(f"Country      : {country}")
    print(f"Days         : {days}")
    # Menggunakan :g agar jika input 1500.0 akan dicetak 1500 tanpa desimal .0
    print(f"Budget       : {budget:g} {currency}")
    print(f"Currency     : {currency}")
    print(f"Travel Month : {travel_month}")


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
