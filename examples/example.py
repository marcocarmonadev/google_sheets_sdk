import asyncio

import httpx

import google_sheets
import google_sheets.core
import google_sheets.core.models


async def main():
    async with httpx.AsyncClient() as http_client:
        client = google_sheets.Client(
            http_client,
            settings=google_sheets.core.models.Settings(),  # type: ignore
        )


if __name__ == "__main__":
    asyncio.run(main())
