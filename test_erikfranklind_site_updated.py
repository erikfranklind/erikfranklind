import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://erikfranklind.github.io/erikfranklind/")

        assert await page.locator('[data-lang="sv"] img.profile').is_visible(), "Svenska profilbilden syns inte"
        assert await page.locator("text=E-handelsproffs & Digital Strateg").is_visible(), "Svensk titel saknas"

        await page.locator('.language-switch a:has-text("English")').click()
        await page.wait_for_timeout(500)

        assert await page.locator('[data-lang="en"] img.profile').is_visible(), "Engelsk profilbild syns inte"
        assert await page.locator("text=E-commerce Expert & Digital Strategist").is_visible(), "Engelsk titel saknas"
        assert await page.locator("text=Listen to the episode").is_visible(), "Poddlänk saknas"
        assert await page.locator("text=Watch the webinar").is_visible(), "Webbinarielänk saknas"
        assert await page.locator("text=Download CV (PDF)").is_visible(), "CV-knapp saknas"

        print("✅ Alla tester passerade!")
        await browser.close()

asyncio.run(run_test())
