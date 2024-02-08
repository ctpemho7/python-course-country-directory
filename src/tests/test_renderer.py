"""
Тестирование функций генерации выходных данных.
"""
import pytest

from renderer import Renderer


@pytest.mark.asyncio
class TestRenderer:
    @pytest.fixture
    def renderer(self, location_info_model_fixture):
        return Renderer(location_info_model_fixture)

    async def test_render(self, renderer):
        country_tab, capital_tab, weather_tab, news_tab = await renderer.render()

        assert len(country_tab.rows) == 6
        assert len(capital_tab.rows) == 4
        assert len(weather_tab.rows) == 6
        assert len(news_tab.rows) == 3
