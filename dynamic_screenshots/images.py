import time
from utils import add_margins


async def process_consent_matching(page, output_file):
    child_key = page.get_by_text("Child", exact=True)
    child_row = child_key.locator("..")
    child_value = await child_row.locator("dd").inner_text()
    await page.get_by_label("Name", exact=True).fill(child_value)
    time.sleep(0.5)
    await page.get_by_role("link", name="Select").click()

    title_key = page.get_by_text(" Link consent response with child record? ")
    title_box = await title_key.element_handle()
    title_box = await title_box.bounding_box()
    title_height = title_box["height"]+24

    details_key = page.get_by_text(" Compare details ", exact=True)
    details_box = await details_key.locator("..").element_handle()
    details_box = await details_box.bounding_box()

    details_box["height"] += title_height
    details_box["y"] -= title_height

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_get_consent(page, output_file):
    child_links = await page.get_by_text("Full name", exact=True).all()
    child_link = child_links[-1]
    parent = child_link.locator("..")
    await parent.locator("a").click()

    await page.get_by_role("button", name="Get consent response").click()
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[0].check()   
    await page.get_by_role("button", name="Continue").click()
    await page.get_by_role("button", name="Continue").click()

    details_key = page.get_by_role("main")
    details_box = await details_key.element_handle()
    details_box = await details_box.bounding_box()

    details_box = add_margins(details_box, 5)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)


IMAGES = [
    # {
    #     "description": "Screenshot of a register attendance page.",
    #     "image_name": "session-attendance.png",
    #     "url_extension": "sessions/1/attendances/unregistered?sort=name&direction=asc",
    #     "screen_size": {    
    #         "width": 1100,
    #         "height": 1080
    #     }
    # },
    # {
    #     "description": "Screenshot of a potential match for an unmatched consent response.",
    #     "image_name": "consent-link.png",
    #     "url_extension": "consent-forms/1",
    #     "screen_size": {    
    #         "width": 700,
    #         "height": 1080
    #     },
    #     "further_processing": process_consent_matching
    # },
    {
        "description": "Screenshot of a potential match for an unmatched consent response.",
        "image_name": "consent-response-paper.png",
        "url_extension": "sessions/1/consents/given",
        "screen_size": {    
            "width": 700,
            "height": 1080
        },
        "further_processing": process_get_consent
    }
]

