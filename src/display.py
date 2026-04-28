from datetime import datetime, timezone, timedelta


def display_weather(data: dict) -> None:
    """Tampilkan data cuaca dalam kotak rapi di terminal."""
    unit_symbol  = "°C" if data["unit"] == "metric" else "°F"
    emoji        = _get_weather_emoji(data["condition"])
    sunrise      = _format_time(data["sunrise"], data["timezone"])
    sunset       = _format_time(data["sunset"],  data["timezone"])
    width        = 44
    border       = "═" * width

    print(f"\n╔{border}╗")
    print(f"║{'🌦️  WEATHER CLI':^{width}}║")
    print(f"╠{border}╣")
    print(f"║  📍 Location  : {data['city']}, {data['country']:<22}║")
    print(f"║  🌡️  Temp      : {data['temp']}{unit_symbol} "
          f"(feels {data['feels_like']}{unit_symbol}){'':<12}║")
    print(f"║  💧 Humidity  : {data['humidity']}%{'':<29}║")
    print(f"║  🌬️  Wind      : {data['wind_speed']} km/h "
          f"{data['wind_dir']:<24}║")
    print(f"║  {emoji} Condition : {data['condition']:<30}║")
    print(f"║  🌅 Sunrise   : {sunrise:<28}║")
    print(f"║  🌇 Sunset    : {sunset:<28}║")
    print(f"╚{border}╝")
    print(f"     Updated: {datetime.now().strftime('%d %b %Y, %H:%M')}\n")


def _format_time(unix_ts: int, tz_offset: int) -> str:
    tz = timezone(timedelta(seconds=tz_offset))
    return datetime.fromtimestamp(unix_ts, tz=tz).strftime("%I:%M %p")


def _get_weather_emoji(condition: str) -> str:
    c = condition.lower()
    if "clear"   in c:                          return "☀️ "
    if "few"     in c or "scattered" in c:      return "⛅"
    if "cloud"   in c:                          return "☁️ "
    if "rain"    in c or "drizzle"   in c:      return "🌧️"
    if "thunder" in c:                          return "⛈️"
    if "snow"    in c:                          return "❄️"
    if "mist"    in c or "fog"       in c:      return "🌫️"
    return "🌡️"
