import asyncio
import json
import tqdm
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

async def take_screenshot(page, url: str, output_file: str):
    await page.goto(url)
    await page.screenshot(path=output_file)

async def main():
    username = "nurse.joy@example.com"
    password = "nurse.joy@example.com"
    base_url = "http://127.0.0.1:4000/"
    
    dynamic_screenshots_dir = os.path.dirname(__file__)
    os.makedirs(os.path.join(dynamic_screenshots_dir,"screenshots"), exist_ok=True)

    metadata_file = os.path.join(dynamic_screenshots_dir, "images.json")

    with open(metadata_file) as data:
        image_metadata = json.load(data)

    for image in image_metadata:
        print(f"Capturing screenshot: {image['image_name']}")
        target_url = base_url + image["url_extension"]
        output_file = f"{dynamic_screenshots_dir}/screenshots/{image['image_name']}"

        async with async_playwright() as p:
            browser = await p.chromium.launch()  # Set headless=True as needed
            context = await browser.new_context(viewport={"width": image["screen_size"]["width"], "height": image["screen_size"]["height"]})
            page = await context.new_page()
            
            # Login to the application
            await login(page, username, password)
            
            # After login, navigate to the target URL and capture the screenshot.
            await take_screenshot(page, target_url, output_file)
            
            await browser.close()
    print("Done")

if __name__ == "__main__":
    asyncio.run(main())