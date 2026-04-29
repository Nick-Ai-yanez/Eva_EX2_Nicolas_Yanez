import asyncio
from services import get_iss, get_astronauts
from utils import is_over_chile

history = []
contador_chile = 0


def print_menu():
    print("\n==============================")
    print("      🚀 ISS TRACKER PRO")
    print("==============================")
    print("1. 🌍 Ver ubicación ISS")
    print("2. 👨‍🚀 Ver astronautas")
    print("3. 📜 Ver historial")
    print("4. ⏱️ Seguimiento en vivo")
    print("5. 📊 Estadísticas")
    print("6. ❌ Salir")


async def ver_iss():
    global contador_chile

    result = await get_iss()

    if result:
        lat, lon, timestamp = result

        print("\n📍 Ubicación actual:")
        print(f"Latitud: {lat}")
        print(f"Longitud: {lon}")
        print(f"Timestamp: {timestamp}")

        history.append((lat, lon))

        if is_over_chile(lat, lon):
            print("🇨🇱 Está sobre Chile!")
            contador_chile += 1


async def ver_astronautas():
    result = await get_astronauts()

    if result:
        total, people = result

        print("\n==============================")
        print("👨‍🚀 INFORMACIÓN DE ASTRONAUTAS")
        print("==============================")
        print(f"\nTotal en el espacio: {total}")

        naves = {}

        for p in people:
            nave = p["craft"]

            if nave not in naves:
                naves[nave] = []

            naves[nave].append(p["name"])

        for nave, nombres in naves.items():
            print(f"\n🚀 Nave: {nave}")
            for nombre in nombres:
                print(f"   - {nombre}")


def ver_historial():
    if not history:
        print("\n⚠️ No hay datos aún")
        return

    print("\n📜 Historial de posiciones:")
    for i, (lat, lon) in enumerate(history, 1):
        print(f"{i}. {lat}, {lon}")


async def seguimiento():
    print("\n⏱️ Seguimiento en vivo (Ctrl + C para salir)\n")

    try:
        while True:
            result = await get_iss()

            if result:
                lat, lon, _ = result
                print(f"📍 {lat}, {lon}")

            await asyncio.sleep(5)

    except KeyboardInterrupt:
        print("\n🔙 Volviendo al menú...")


def ver_estadisticas():
    print("\n📊 Estadísticas:")
    print(f"Veces sobre Chile: {contador_chile}")
    print(f"Registros guardados: {len(history)}")


async def main():
    while True:
        print_menu()
        op = input("👉 Opción: ")

        if op == "1":
            await ver_iss()

        elif op == "2":
            await ver_astronautas()

        elif op == "3":
            ver_historial()

        elif op == "4":
            await seguimiento()

        elif op == "5":
            ver_estadisticas()

        elif op == "6":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida")


asyncio.run(main())