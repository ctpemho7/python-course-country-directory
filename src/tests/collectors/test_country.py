"""
Тестирование функций сбора информации о странах.
"""
import pytest

from collectors.collector import CountryCollector


@pytest.mark.asyncio
class TestCountryCollector:
    """
    Тестирование коллектора для получения информации о странах.
    """

    @pytest.fixture
    def collector(self, mocker):
        mocker.patch(
            "collectors.collector.CountryCollector.cache_invalid", return_value=False
        )
        mocker.patch(
            "collectors.collector.CountryCollector.get_file_path",
            return_value=self.media_path,
        )
        return CountryCollector()

    media_path = "tests/mocks/country.json"

    async def test_collect_countries(self, collector):
        result = await collector.collect()
        assert len(result) == 49

    async def test_read_countries(self, mocker, collector):
        result = await collector.read()
        assert len(result) == 49
