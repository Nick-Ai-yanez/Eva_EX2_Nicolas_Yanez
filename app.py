import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"
ASTRO_URL = "http://api.open-notify.org/astros.json"

print("===================================")
print("ISS TRACKER + ASTRONAUTAS")
print("===================================")

try:
    # =========================
    # ISS
    # =========================
    response_iss = requests.get(ISS_URL, timeout=10)

    response_iss.raise_for_status()

    data_iss = response_iss.json()

    latitude = data_iss["iss_position"]["latitude"]
    longitude = data_iss["iss_position"]["longitude"]
    timestamp = data_iss["timestamp"]

    print("\n UBICACIÓN ISS")
    print(f"Latitud: {latitude}")
    print(f"Longitud: {longitude}")
    print(f"Timestamp: {timestamp}")

    # =========================
    # ASTRONAUTAS
    # =========================
    response_ast = requests.get(ASTRO_URL, timeout=10)

    response_ast.raise_for_status()

    data_ast = response_ast.json()

    total = data_ast["number"]

    print("\n ASTRONAUTAS EN EL ESPACIO")
    print(f"Total: {total}")

    for person in data_ast["people"]:
        print(f"- {person['name']} ({person['craft']})")

except requests.exceptions.Timeout:
    print("❌ ERROR: Timeout de conexión")

except requests.exceptions.ConnectionError:
    print("❌ ERROR: Problema de conexión")

except requests.exceptions.HTTPError:
    print("❌ ERROR: Error HTTP")

except KeyError:
    print("❌ ERROR: Datos incompletos")

except Exception as e:
    print(f"❌ ERROR GENERAL: {e}")