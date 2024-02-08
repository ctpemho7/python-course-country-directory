"""
Тестирование функций клиента для получения информации о погоде.
"""
import pytest

from clients.news import NewsClient
from settings import API_KEY_NEWSAPI


@pytest.mark.asyncio
class TestCurrencyCountry:
    """
    Тестирование клиента для получения информации о валюте.
    """

    base_url = "https://newsapi.org/v2/top-headlines"

    @pytest.fixture
    def client(self):
        return NewsClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_rates(self, mocker, client):
        mocker.patch("clients.news.NewsClient._request")

        await client.get_news("test")
        client._request.assert_called_with(
            f"{self.base_url}?pageSize=3&country=test&apiKey={API_KEY_NEWSAPI}"
        )
