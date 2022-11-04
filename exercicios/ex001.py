import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://nasa.gov')
    await page.screenshot({'path': 'nasa.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())