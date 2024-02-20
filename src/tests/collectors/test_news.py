"""
Тестирование функций сбора информации о новостях.
"""
import pytest

from collectors.collector import NewsCollector


@pytest.mark.asyncio
class TestWeatherCollector:
    """
    Тестирование коллектора для получения информации о странах.
    """

    @pytest.fixture
    def collector(self):
        return NewsCollector()

    media_path = "tests/mocks/news/pl.json"

    async def test_read_news(self, mocker, collector, news_model_fixture):
        mocker.patch(
            "collectors.collector.NewsCollector.get_file_path",
            return_value=self.media_path,
        )

        result = await collector.read(news_model_fixture)

        assert len(result) == 3
        assert (
            result[0].title
            == "Tragiczny pożar w Siemianowicach Śląskich. Nie żyje 4,5-letnie dziecko - RMF 24"
        )
        assert (
            result[1].title
            == "Węgry zagłosują nad przyjęciem Szwecji do NATO. Wymowny gest Orbana - BusinessInsider"
        )
        assert (
            result[2].title
            == "Tabela wzrostów emerytur od marca - Ministerstwo podało dane! Mamy wyliczenia waloryzacji emerytur "
            "- Gazeta Pomorska"
        )
