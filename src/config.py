import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"


def load_config() -> dict:
    """Baca config dari config.json."""
    if not CONFIG_PATH.exists():
        default = {
            "default_city": "Jakarta",
            "unit": "metric",
            "favorite_cities": ["Jakarta", "Surabaya", "Bandung"]
        }
        save_config(default)
        return default

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config: dict) -> None:
    """Simpan config ke config.json."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def get_default_city() -> str:
    return load_config().get("default_city", "Jakarta")


def get_unit() -> str:
    return load_config().get("unit", "metric")


def get_favorites() -> list:
    return load_config().get("favorite_cities", [])


def add_favorite(city: str) -> None:
    config = load_config()
    if city not in config["favorite_cities"]:
        config["favorite_cities"].append(city)
        save_config(config)
        print(f"✅ '{city}' ditambahkan ke favorit!")
    else:
        print(f"⚠️  '{city}' sudah ada di favorit.")


def set_default_city(city: str) -> None:
    config = load_config()
    config["default_city"] = city
    save_config(config)
    print(f"✅ Default kota diubah ke '{city}'")
