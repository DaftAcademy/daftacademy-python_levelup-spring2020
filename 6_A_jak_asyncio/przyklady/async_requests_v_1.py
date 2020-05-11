import asyncio
import time

import httpx


responses = []
urls_f_name = 'urls'


async def main():
    with open(urls_f_name, 'r') as f:
        async with httpx.AsyncClient(timeout=15) as client:
            for line in f.readlines():
                print(f'Checking {line}')
                resp = await client.get(line)
                responses.append(resp)    


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'elapsed: {end - start} seconds')
