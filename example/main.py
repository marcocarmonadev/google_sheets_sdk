import asyncio

import httpx

from google_sheets_sdk import GoogleSheetClient


async def main():
    async with httpx.AsyncClient() as http_client:
        google_sheet_client = GoogleSheetClient(http_client)


if __name__ == "__main__":
    asyncio.run(main())
