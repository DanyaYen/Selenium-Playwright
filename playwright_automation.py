import asyncio
from playwright.async_api import async_playwright, Playwright, expect

async def run_full_checkout_scenario_slower(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=700)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://www.saucedemo.com/")

    await page.locator("[data-test='username']").fill("standard_user")
    await page.locator("[data-test='password']").fill("secret_sauce")
    await page.locator("[data-test='login-button']").click()

    await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    first_item_add_to_cart_button = page.locator(".inventory_item button[id^='add-to-cart-']").first
    await first_item_add_to_cart_button.click()

    await page.locator(".shopping_cart_link").click()
    await expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    await page.locator("[data-test='checkout']").click()
    await expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    await page.locator("[data-test='firstName']").fill("TestFirstName")
    await page.locator("[data-test='lastName']").fill("TestLastName")
    await page.locator("[data-test='postalCode']").fill("12345")

    await page.locator("[data-test='continue']").click()
    await expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    await expect(page.locator(".summary_total_label")).to_be_visible()

    await page.wait_for_timeout(3000) 

    await page.locator("[data-test='finish']").click()
    await expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    thank_you_header = page.locator(".complete-header")
    await expect(thank_you_header).to_have_text("Thank you for your order!")

    await page.locator("[data-test='back-to-products']").click()
    await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    await page.wait_for_timeout(2000)

    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run_full_checkout_scenario_slower(playwright)

if __name__ == "__main__":
    asyncio.run(main())