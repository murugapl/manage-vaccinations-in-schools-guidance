import asyncio
import json
import datetime
import os
from playwright.async_api import async_playwright

async def login(page, username: str, password: str):
    # Replace with your app's login URL and adjust selectors as needed.
    await page.goto("http://127.0.0.1:4000/")
    await page.get_by_text("Start now").click()
    await page.get_by_label("Email address").fill(username)
    await page.get_by_label("Password", exact=True).fill(password)
    await page.get_by_role("button", name="Log in").click()
    await page.wait_for_url("**/users/organisations/new", timeout=1000)
    await page.pause()
    await page.get_by_role("heading", name="SAIS Organisation 1 (R1L)").click()
    await page.wait_for_url("**/dashboard", timeout=1000)

async def take_screenshot(page, url: str, step_id: str, description: str, output_file: str):
    await page.goto(url)
    await page.screenshot(path=output_file)
    metadata = {
        "id": step_id,
        "url": url,
        "image": output_file,
        "description": description,
        # "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }
    return metadata

async def main():
    username = "nurse.joy@example.com"
    password = "nurse.joy@example.com"
    target_url = "http://127.0.0.1:4000/programmes/hpv/vaccination-records"
    step_id = "vaccination-reccords"
    description = "Target page after login"
    output_file = "screenshots/step-1.png"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()  # Set headless=True as needed
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        # Login to the application
        await login(page, username, password)
        
        # After login, navigate to the target URL and capture the screenshot.
        metadata = await take_screenshot(page, target_url, step_id, description, output_file)
        
        await browser.close()

        #   Save the metadata to a JSON file.
        with open("metadata.json", "w") as f:
            json.dump(metadata, f, indent=4)
        print("Logged in, captured screenshot, and saved metadata.")

if __name__ == "__main__":
    asyncio.run(main())