# 🌦️ Weather CLI

> Check real-time weather for any city directly from your terminal.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## ✨ Features

- 🌡️ Real-time temperature with "feels like"
- 💧 Humidity & wind speed + direction
- 🌅 Sunrise & sunset time (local timezone)
- ⭐ Save favorite cities in `config.json`
- 🎨 Clean box-style terminal UI
- ❗ Proper error handling

## 🚀 Quick Start

```bash
# 1. Clone repo
git clone https://github.com/XCarrzX/weather-cli.git
cd weather-cli

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup API key
cp .env.example .env
# Buka .env dan isi API key kamu dari openweathermap.org

# 4. Jalankan!
python main.py Jakarta
```

## 📖 Usage

```bash
python main.py                          # Pakai kota default (Jakarta)
python main.py Bali                     # Cek kota tertentu
python main.py London --unit imperial   # Pakai Fahrenheit
python main.py --favorites              # Cuaca semua kota favorit
python main.py --add-favorite Bali      # Tambah Bali ke favorit
python main.py --set-default Bali       # Ubah kota default
```

## 📁 Project Structure

```
weather-cli/
├── src/
│   ├── weather.py      # Ambil data dari API
│   ├── display.py      # Tampilan terminal
│   └── config.py       # Manajemen config & favorit
├── main.py             # Entry point CLI
├── config.json         # Kota default & favorit (editable)
├── .env.example        # Template API key
└── requirements.txt    # Dependencies
```

## 🔑 Get Free API Key

1. Daftar di [openweathermap.org](https://openweathermap.org/api)
2. Verifikasi email
3. Buka menu **API Keys** di dashboard
4. Copy API key → paste ke file `.env`

## 🛠️ Tech Stack

- **Python 3.10+**
- **requests** — HTTP calls ke OpenWeatherMap
- **python-dotenv** — Load API key dari `.env`

## 📄 License

MIT License — bebas digunakan & dimodifikasi.
