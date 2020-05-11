import asyncio
import time

import httpx


responses = []
urls_f_name = 'urls'
urls_f_name = 'urls_2'

partials = []
async def get(url, client):
    print(f'Checking {url}')
    start = time.time()
    resp = await client.get(url)
    end = time.time()
    partials.append(end-start)
    responses.append(resp)

async def main():
    with open(urls_f_name, 'r') as f:
        async with httpx.AsyncClient(timeout=15) as client:
            coroutines = []
            for line in f.readlines():
                coroutines.append(get(line, client))
            await asyncio.gather(*coroutines)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'elapsed: {end - start} seconds')
    print(f'total partials: {sum(partials)}')
