from playwright.sync_api import Page


def test_login_form(page: Page):
    # 1. Открываем сайт
    page.goto("https://lkfl.tatenergosbyt.ru")

    # 2. Ждем появления поля ввода логина
    page.locator("input[type='text']").wait_for(state="visible")

    # 3. Печатаем логин последовательно с задержкой в 150 миллисекунд
    page.locator("input[type='text']").press_sequentially("test_login", delay=150)

    # 4. Печатаем пароль последовательно с задержкой
    page.locator("input[type='password']").press_sequentially("123456789", delay=150)

    # 5. Кликаем по кнопке «Войти»
    page.get_by_role("button", name="Войти").click()

    # Пауза, чтобы увидели результат перед закрытием
    page.wait_for_timeout(5000)
