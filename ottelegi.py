import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.divan.ru/product/svetilnik-potolochnyj-matthew']

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        # Инициализация драйвера
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        # Открываем страницу с помощью Selenium
        self.driver.get(response.url)
        time.sleep(2)  # Ждем, чтобы страница загрузилась

        # Извлечение данных
        name = self.driver.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = self.driver.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        href = self.driver.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')

        # Генерация результата
        yield {
            'name': name,
            'price': price,
            'url': href
        }

        # Закрываем драйвер после завершения
        self.driver.quit()
