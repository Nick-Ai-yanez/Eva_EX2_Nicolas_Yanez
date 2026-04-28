import aiohttp
import asyncio

async def fetch(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:

                if response.status == 200:
                    return await response.json()

                elif response.status == 404:
                    print("❌ Error 404")

                else:
                    print(f"⚠️ Error HTTP {response.status}")

    except asyncio.TimeoutError:
        print("⏱️ Timeout")
    except aiohttp.ClientConnectionError:
        print("🌐 Error de conexión")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None


async def get_iss():
    url = "http://api.open-notify.org/iss-now.json"
    data = await fetch(url)

    if data:
        return (
            data["iss_position"]["latitude"],
            data["iss_position"]["longitude"],
            data["timestamp"]
        )
    return None


async def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    data = await fetch(url)

    if data:
        return data["number"], data["people"]
    return None