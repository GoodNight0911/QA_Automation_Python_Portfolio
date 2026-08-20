from playwright.sync_api import Page


def test_add_phone_to_cart(page: Page):
    # 1. Открываем интернет-магазин гаджетов
    page.goto("https://demoblaze.com")

    # 2. Находим по тексту ссылку на Samsung Galaxy S6 и кликаем по ней
    page.get_by_role("link", name="Samsung galaxy s6").click()

    # 3. Находим кнопку "Add to cart" по её тексту и нажимаем
    # Используем точное совпадение текста
    page.get_by_text("Add to cart").click()

    # 4. Сайт выдаст браузерное alert-окно,
    # мы просим Playwright дождаться появления диалога и автоматически нажать "ОК"
    page.on("dialog", lambda dialog: dialog.accept())

    # Пауза 4 секунды, чтобы увидеть, как нажалась кнопка добавления(в рабочих задачах не использовать)
    # page.wait_for_timeout(4000)

    # 5. Кликаем по кнопке "Cart" (Корзина) в верхнем навигационном меню
    page.get_by_role("link", name="Cart", exact=True).click()

    # 6. Ждем, пока в таблице корзины появится строка с нашим телефоном
    page.locator("td:has-text('Samsung galaxy s6')").wait_for(state="visible")

    # 7. ГЛАВНАЯ ПРОВЕРКА: убеждаемся, что этот текст физически виден на экране
    assert page.locator("td:has-text('Samsung galaxy s6')").is_visible()
