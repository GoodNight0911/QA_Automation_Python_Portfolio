from playwright.sync_api import Page


def test_google_search(page: Page):

    # Открываем сайт
    page.goto("https://google.com")

    # Находим поисковую строку по ее имени (name="q") и вводим текст
    page.locator("textarea[name='q']").fill("Python")

    # Нажимает клавишу Enter на клавиатуре для старта поиска
    page.locator("textarea[name='q']").press("Enter")

    # Проверяем, что на новой странице в заголовке вкладки появилось слово "Python"
    # assert "Python" in page.title()

    # Ждем, пока в URL адресе странице появится слово "Python"
    page.wait_for_url("**/search?q=Python*")
