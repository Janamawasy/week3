import requests
import json
import aiohttp
import asyncio

def fetch_data(api):
    data = requests.get(api).json()
    return data['near_earth_objects']


def load_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

async def fetch_async_data(api):
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as response:
            data = await response.json()
            return data['near_earth_objects']

async def fetch_month_data(urls):
    tasks = [fetch_async_data(url) for url in urls]
    # *tasks - unpack the list to individual arguments
    res = await asyncio.gather(*tasks)
    return res