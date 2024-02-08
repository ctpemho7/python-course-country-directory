"""
Тестирование функций поиска (чтения) собранной информации в файлах.
"""
import pytest

from reader import Reader


@pytest.mark.asyncio
class TestReader:

    country_path = "tests/mocks/country.json"
    currency_path = "tests/mocks/currency_rates.json"
    news_path = "tests/mocks/news/pl.json"
    weather_path = "tests/mocks/weather/warsaw_pl.json"

    city_to_find = "Warsaw"
    city_not_found = "Azkaban"

    @pytest.fixture
    def reader(self, mocker):
        # country
        mocker.patch(
            "collectors.collector.CountryCollector.cache_invalid", return_value=False
        )
        mocker.patch(
            "collectors.collector.CountryCollector.get_file_path",
            return_value=self.country_path,
        )
        # currency
        mocker.patch(
            "collectors.collector.CurrencyRatesCollector.get_file_path",
            return_value=self.currency_path,
        )
        # news
        mocker.patch(
            "collectors.collector.NewsCollector.get_file_path",
            return_value=self.news_path,
        )
        # weather
        mocker.patch(
            "collectors.collector.WeatherCollector.get_file_path",
            return_value=self.weather_path,
        )
        return Reader()

    async def test_read_find_city(self, reader):
        result = await reader.find(self.city_to_find)
        assert result.location.capital == self.city_to_find

    async def test_read_not_find_city(self, reader):
        result = await reader.find(self.city_not_found)
        assert result is None
