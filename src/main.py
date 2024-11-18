import asyncio
from src.infrastructure import FastAPIServer


async def main():
    await FastAPIServer().run()


if __name__ == "__main__":
    asyncio.run(main())
