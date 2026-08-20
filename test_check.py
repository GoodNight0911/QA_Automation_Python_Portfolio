# Наша функция, которую мы проверяем (имитация логина)
def check_login(username, password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False


# Первый автотест (на успешный вход)
def test_login_success():
    assert check_login("admin", "12345") == True


# Второй автотест (на ошибку при неверном пароле)
def test_login_fail():
    assert check_login("admin", "wrong_pass") == False
