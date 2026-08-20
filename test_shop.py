from playwright.sync_api import Page


def test_add_phone_to_cart(page: Page):
    # 1. Открываем интернет-магазин гаджетов
    page.goto("https://demoblaze.com")

    # 2. Переходим в карточку Samsung
    page.get_by_role("link", name="Samsung galaxy s6").click()

    # 3. СНАЧАЛА включаем перехватчик всплывающего окна (dialog)
    page.on("dialog", lambda dialog: dialog.accept())

    # 4. Теперь кликаем "Add to cart" — окно выскочит и тут же закроется само
    page.get_by_text("Add to cart").click()

    # 5. Кликаем по кнопке "Cart" (Корзина) в верхнем меню
    page.get_by_role("link", name="Cart", exact=True).click()

    # 6. Ждем правильный URL
    page.wait_for_url("**/cart.html")

    # 7. Проверяем, что адрес сайта теперь точно равен странице корзины
    assert page.url == "https://demoblaze.com/cart.html"
