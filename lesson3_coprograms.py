import asyncio
from time import time


async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print('Get pages for {}'.format(site_name))
    return range(1, 4)


async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return "Data from page {} ({})".format(page,site_name)


async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        print(site_name, page)


start = time()

spider = [
    asyncio.ensure_future(spider('Blog')),
    asyncio.ensure_future(spider('News')),
    asyncio.ensure_future(spider('Forum'))
]

event_loop = asyncio.get_event_loop()
now = event_loop.time()
event_loop.call_soon(loader, 'url1')
event_loop.call_at(now + 1.9, loader, 'url2')
event_loop.run_until_complete(asyncio.gather(*spider))

event_loop.close()

print(time() - start)
