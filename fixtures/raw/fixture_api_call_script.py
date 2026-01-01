import requests
import json
import os

API_KEY = "8a10cefc9ecef799d541b4777edbefcd"  # <-- replace if you regenerate
LEAGUE_ID = 39
SEASON = 2025

url = "https://v3.football.api-sports.io/fixtures"

# For direct API-Sports (api-sports.io):
headers = {
    "x-apisports-key": API_KEY,
    "Accept": "application/json"
}

params = {
    "league": LEAGUE_ID,
    "season": SEASON
}

print(f"Requesting fixtures for league {LEAGUE_ID}, season {SEASON} ...")
r = requests.get(url, headers=headers, params=params, timeout=30)

print("Status:", r.status_code)
print("URL:", r.url)

try:
    data = r.json()
    print("Results:", data.get("results"))
    print("Errors:", data.get("errors"))

    # Show first fixture if available
    if data.get("response"):
        print("Sample fixture:", data["response"][0])

    # -------- SAVE TO FILE --------
    save_dir = r"C:\Users\Sam\OneDrive\Documents\football_stats\raw\fixtures"
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, f"fixtures_{SEASON}.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Full fixtures JSON saved to {save_path}")

except Exception:
    print("Raw response:", r.text[:500])
