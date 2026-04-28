import asyncio
from services import get_iss, get_astronauts
from utils import is_over_chile

async def main():
    while True:
        print("\n=== ISS TRACKER ===")
        print("1. Ver ISS")
        print("2. Ver astronautas")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            result = await get_iss()

            if result:
                lat, lon, timestamp = result

                print(f"\nLatitud: {lat}")
                print(f"Longitud: {lon}")
                print(f"Timestamp: {timestamp}")

                if is_over_chile(lat, lon):
                    print("🇨🇱 Está sobre Chile!")

        elif op == "2":
            result = await get_astronauts()

            if result:
                total, people = result

                print(f"\nPersonas en el espacio: {total}")
                for p in people:
                    print(f"- {p['name']} ({p['craft']})")

        elif op == "3":
            print("Saliendo...")
            break

        else:
            print("❌ Opción inválida")

asyncio.run(main())