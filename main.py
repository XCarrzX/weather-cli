import argparse
import sys
from src.weather import get_weather
from src.display import display_weather
from src.config  import (load_config, get_default_city,
                          get_unit, get_favorites,
                          add_favorite, set_default_city)


def main():
    config = load_config()

    parser = argparse.ArgumentParser(
        description="🌦️  Weather CLI — Cek cuaca dari terminal!",
        epilog="Contoh: python main.py Jakarta --unit metric"
    )
    parser.add_argument("city", nargs="?",
                        help="Nama kota (contoh: Jakarta, London)")
    parser.add_argument("--unit", choices=["metric", "imperial"],
                        default=config["unit"],
                        help="Satuan suhu: metric=Celsius, imperial=Fahrenheit")
    parser.add_argument("--favorites", action="store_true",
                        help="Tampilkan cuaca semua kota favorit")
    parser.add_argument("--add-favorite", metavar="CITY",
                        help="Tambah kota ke daftar favorit")
    parser.add_argument("--set-default", metavar="CITY",
                        help="Set kota default")

    args = parser.parse_args()

    # Mode: set default city
    if args.set_default:
        set_default_city(args.set_default)
        return

    # Mode: tambah favorit
    if args.add_favorite:
        add_favorite(args.add_favorite)
        return

    # Mode: tampilkan semua favorit
    if args.favorites:
        favorites = get_favorites()
        if not favorites:
            print("⚠️  Belum ada kota favorit.")
            print("    Tambah dengan: python main.py --add-favorite NamaKota")
            return
        for city in favorites:
            try:
                data = get_weather(city, args.unit)
                display_weather(data)
            except Exception as e:
                print(f"❌ {city}: {e}")
        return

    # Mode: cek 1 kota
    city = args.city or get_default_city()
    print(f"\n⏳ Mengambil data cuaca untuk '{city}'...")

    try:
        data = get_weather(city, args.unit)
        display_weather(data)
    except (ValueError, ConnectionError) as e:
        print(f"\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
