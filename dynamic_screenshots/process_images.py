from utils import add_margins, remove_top_banner,remove_top_banner_and_footer


async def process_consent_matching(page, output_file):
    match_links = await page.get_by_role("link", name="Match", exact=True).all()
    await match_links[0].click()
    child_key = page.get_by_text("Full name", exact=True)
    child_row = child_key.locator("..")
    child_value = await child_row.locator("dd").inner_text()
    search_input = page.locator('#search-form-q-field')
    await search_input.fill(child_value)
    await page.get_by_role("button", name="Search").click()
    await page.click(f'a:text("{child_value}")')

    title_key = page.get_by_text(" Link consent response with child record? ")
    title_box = await title_key.element_handle()
    title_box = await title_box.bounding_box()
    title_height = title_box["height"]+24

    details_key = page.locator('div.nhsuk-card-group')
    details_box = await details_key.element_handle()
    details_box = await details_box.bounding_box()

    details_box["height"] += title_height
    details_box["y"] -= title_height

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_get_consent(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    if child:
        await child.click()

    await page.get_by_role("button", name="Get consent response").click()
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[0].check()   
    await page.get_by_role("button", name="Continue").click()
    await page.get_by_role("button", name="Continue").click()

    details_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_school_move_review(page, output_file):
    first_link = await page.query_selector("a[href*='Review']")
    if first_link:
        first_link.click()
    
    details_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_pre_screening(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    if child:
        await child.click()

    headers = await page.query_selector_all(".nhsuk-card__content")
    if headers:
        header = headers[-1]

    header_box = await header.bounding_box()

    header_box = add_margins(header_box, 16)

    await page.screenshot(path=output_file, clip=header_box, full_page=True)

async def process_get_gillick_competent_consent(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    if child:
        await child.click()
    
    await page.get_by_role("link", name="Gillick").click()
    radio_buttons = await page.locator("[type='radio']").all()    
    for button in radio_buttons:
        parent = button.locator("..")
        inner_text = await parent.locator("label").inner_text()
        if "Yes" in inner_text:
            await button.check()
    await page.get_by_role("button", name="your assessment").click()
    await page.get_by_role("button", name="Get consent response").click()

    header = page.get_by_role("heading", name=" Who are you trying to get consent from? ")
    parent = header.locator("..")
    header_box = await parent.element_handle()
    header_box = await header_box.bounding_box()

    header_box = add_margins(header_box, 16)

    await page.screenshot(path=output_file, clip=header_box, full_page=True)

async def process_sessions_add_dates(page, output_file):
    change_links = await page.query_selector_all("a.nhsuk-link:has-text('Change')")
    if len(change_links) > 1:
        await change_links[1].click()
    
    delete_buttons = await page.get_by_text("Delete", exact=True).all()    
    for button in delete_buttons:
        await button.click()
    
    await page.get_by_text("Continue", exact=True).click()
    await page.get_by_text("Schedule sessions", exact=True).click()


    body_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, full_page=True, clip=body_box)

async def process_session_no_consent(page, output_file):
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[1].check()

    await page.get_by_text("Update results", exact=True).click()

    body_box = await remove_top_banner(page)

    await page.screenshot(path=output_file, clip=body_box)
