import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WebScraper(metaclass=Singleton):
    def __init__(self):
        self.session = requests.Session()

    def obtener_deuda(self, url, codigo_cliente, correo, dni):
        payload = {
            'codigo': codigo_cliente,
            'email': correo,
            'dni': dni,
        }

        response = self.session.post(url, data=payload)
        soup = BeautifulSoup(response.content, "html.parser")
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        total_a_pagar_label = soup.find("th", string="TOTAL A PAGAR: ")
        total_a_pagar_value = None
        if total_a_pagar_label:
            total_a_pagar_value = total_a_pagar_label.find_next_sibling("th").text.strip()

        return total_a_pagar_value
