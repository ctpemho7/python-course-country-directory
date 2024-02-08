"""
Тестирование функций сбора информации о курсах валют.
"""
import pytest

from collectors.collector import CurrencyRatesCollector


@pytest.mark.asyncio
class TestCountryCollector:
    """
    Тестирование коллектора для получения информации о странах.
    """

    @pytest.fixture
    def collector(self):
        return CurrencyRatesCollector()

    media_path = "tests/mocks/currency_rates.json"

    async def test_read_rates(self, mocker, collector):
        mocker.patch(
            "collectors.collector.CurrencyRatesCollector.get_file_path",
            return_value=self.media_path,
        )

        result = await collector.read()
        assert result.base == "RUB"
        assert result.date == "2024-02-05"
        assert len(result.rates) == 169
