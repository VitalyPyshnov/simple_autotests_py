from selenium import webdriver #импортим веб-драйвер
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time  # Добавляем модуль time для управления временем


# Указываем путь до драйвера ChromeDriver
driver_path = '/Users/vitalikpysnov/chromedriver/chromedriver'

# Настраиваем браузер
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Запускаем браузер в фоновом режиме (не отображается окно браузера)

# Инициализируем сервис для ChromeDriver
chrome_service = Service(driver_path)

# Инициализируем браузер
browser = webdriver.Chrome(service=chrome_service, options=options)

# Переходим на страницу авторизации
browser.get('https://agroros-ul-portal.stands.isimple.ru/')

try:
    # Ждем загрузки страницы и находим элементы формы авторизации
    username_input = WebDriverWait(browser, 40).until(
        EC.presence_of_element_located((By.ID, 'login'))
    )
    password_input = WebDriverWait(browser, 40).until(
        EC.presence_of_element_located((By.ID, 'current-password'))
    )
    submit_button = WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/app-auth/div/div/app-login-form/div/form/app-button/div/div/div/span'))
    )

    # Выводим сообщения для отслеживания прогресса
    print("Нашли поле Логин.")
    print("Нашли поле Пароль.")
    print("Нашли Кнопку Входа.")

    # Вводим задержку в 5 секунд перед вводом логина и пароля
    time.sleep(3)


    # Вводим логин и пароль
    username_input.send_keys('clntPrPvN')
    time.sleep(2)
    password_input.send_keys('clntPrPvN')
    time.sleep(2)

    # Нажимаем кнопку входа
    submit_button.click()

    # Ждем перенаправления на главную страницу после успешной авторизации
    WebDriverWait(browser, 100).until(
        EC.url_contains('/main')
    )

    print('Авторизация прошла успешно!')
except Exception as e:
    print(f'Ошибка авторизации: {e}')
finally:
    # Закрываем браузер
    browser.quit()