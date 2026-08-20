from playwright.sync_api import Page


def test_google_title(page: Page):

    # Робот сам открывает сайт Google
    page.goto("https://google.com")

    # Робот проверяет, заголовок вкладки совпадает со словом "Google"
    assert page.title() == "Google"
