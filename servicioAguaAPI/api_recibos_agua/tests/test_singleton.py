
from django.test import TestCase
from api_recibos_agua.scraping import WebScraper
from django.conf import settings

settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
})


def test_singleton():
    scraper1 = WebScraper()
    scraper2 = WebScraper()
    scraper3 = WebScraper()
    
    print(scraper1 is scraper2)  # Debería imprimir: True
    print(scraper1 is scraper3)  # Debería imprimir: True

test_singleton()
