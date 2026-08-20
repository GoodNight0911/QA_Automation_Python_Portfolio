from playwright.sync_api import Page


def test_laptop_order(page: Page):

    # Открываем сайт магазина гаджетов
    page.goto("https://demoblaze.com")

    # Переходим в раздел Laptops(Ноутбуки)
    page.get_by_role("link", name="Laptops").click()

    # Переходим в карточку Sony vaio i5
    page.get_by_role("link", name="Sony vaio i5").click()

    # СНАЧАЛА включаем перехватчик всплывающего окна (это строка должна идти перед кликом, караулит окно) (dialog)
    page.on("dialog", lambda dialog: dialog.accept())

    # Теперь кликаем "Add to cart" — окно выскочит и тут же закроется само
    page.get_by_text("Add to cart").click()

    # Кликаем по кнопке "Cart" (Корзина) в верхнем меню
    page.get_by_role("link", name="Cart", exact=True).click()

    # Кликаем по кнопке "Place Order"
    page.get_by_role("button", name="Place Order").click()

    # Ждем, пока заголовок всплывающего окна станет видимым
    page.get_by_text("Place order").first.wait_for(state="visible")

    # ГЛАВНАЯ ПРОВЕРКА: утверждаем, что заголовок виден на экране
    assert page.get_by_text("Place order").first.is_visible()
