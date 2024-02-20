"""
Тестирование функций сбора информации о погоде.
"""
import pytest

from collectors.collector import WeatherCollector


@pytest.mark.asyncio
class TestWeatherCollector:
    """
    Тестирование коллектора для получения информации о странах.
    """

    @pytest.fixture
    def collector(self):
        return WeatherCollector()

    media_path = "tests/mocks/weather/warsaw_pl.json"

    async def test_read_weather(self, mocker, collector, location_model_fixture):
        mocker.patch(
            "collectors.collector.WeatherCollector.get_file_path",
            return_value=self.media_path,
        )

        result = await collector.read(location_model_fixture)

        assert result.temp == 8.38
        assert result.pressure == 999
        assert result.humidity == 80
        assert result.visibility == 10000
        assert result.wind_speed == 10.29
        assert result.description == "облачно с прояснениями"
        assert result.offset_seconds == 3600
