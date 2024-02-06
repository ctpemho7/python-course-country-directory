"""
Функции для формирования выходной информации.
"""

import datetime
from decimal import ROUND_HALF_UP, Decimal
from textwrap import fill
from typing import Optional

from prettytable import PrettyTable

from collectors.models import LocationInfoDTO


class Renderer:
    """
    Генерация результата преобразования прочитанных данных.
    """

    def __init__(self, location_info: LocationInfoDTO) -> None:
        """
        Конструктор.

        :param location_info: Данные о географическом месте.
        """

        self.location_info = location_info

    async def render(self) -> tuple[PrettyTable, ...]:
        """
        Форматирование прочитанных данных.

        :return: Результат форматирования
        """

        country_tab = PrettyTable(["Поле", "Значение"], align="l")
        capital_tab = PrettyTable(["Поле", "Значение"], align="l")
        weather_tab = PrettyTable(["Поле", "Значение"], align="l")
        news_tab = PrettyTable(
            ["Название", "Автор", "Описание", "Опубликовано", "Ссылка"], align="l"
        )

        # инфо о стране
        country_tab.add_row(["Страна", f"{self.location_info.location.name}"])
        country_tab.add_row(["Площадь", f"{await self._format_area()} км²"])
        country_tab.add_row(["Регион", f"{self.location_info.location.subregion}"])
        country_tab.add_row(["Языки", f"{await self._format_languages()}"])
        country_tab.add_row(
            ["Население страны", f"{await self._format_population()} чел."]
        )
        country_tab.add_row(["Курсы валют", f"{await self._format_currency_rates()}"])

        # инфо о столице
        capital_tab.add_row(["Столица", f"{self.location_info.location.capital}"])
        capital_tab.add_row(
            ["Широта столицы", f"{self.location_info.location.capital_latitude}"]
        )
        capital_tab.add_row(
            ["Долгота столицы", f"{self.location_info.location.capital_longitude}"]
        )
        capital_tab.add_row(["Часовой пояс", f"{await self._get_timezone()}"])

        # Погода в столице
        weather_tab.add_row(["Время", f"{await self._format_current_time()}"])
        weather_tab.add_row(["Температура", f"{self.location_info.weather.temp} °C"])
        weather_tab.add_row(["Погода", f"{self.location_info.weather.description}"])
        weather_tab.add_row(["Влажность", f"{self.location_info.weather.humidity}%"])
        weather_tab.add_row(["Видимость", f"{await self._format_visibility()} км"])
        weather_tab.add_row(
            ["Скорость ветра", f"{self.location_info.weather.wind_speed} м/с"]
        )

        # Новости
        for news_entry in self.location_info.news:
            news_tab.add_row(
                [
                    fill(news_entry.title, width=50),
                    news_entry.author,
                    fill(
                        await self._format_description(news_entry.description), width=50
                    ),
                    fill(
                        await self._format_publication_date(news_entry.published_at),
                        width=10,
                    ),
                    fill(news_entry.url, width=50),
                ]
            )

        return country_tab, capital_tab, weather_tab, news_tab

    async def _format_publication_date(self, date: str) -> str:
        """
        Форматирование описания новости.

        :return:
        """
        print(date)
        render_time = datetime.datetime.strptime(
            date, "%Y-%m-%dT%H:%M:%SZ"
        ) + datetime.timedelta(seconds=self.location_info.weather.offset_seconds)
        return render_time.strftime("%X, %x")

    @staticmethod
    async def _format_description(description: Optional[str]) -> str:
        """
        Форматирование описания новости.

        :return:
        """
        if description is None:
            return "-"
        return description

    async def _get_timezone(self) -> str:
        """
        Форматирование информации о времени.

        :return:
        """
        offset_hours = self.location_info.weather.offset_seconds / 3600.0
        return "UTC{:+d}:{:02d}".format(int(offset_hours), int((offset_hours % 1) * 60))

    async def _format_current_time(self) -> str:
        """
        Форматирование информации о времени.

        :return:
        """
        render_time = datetime.datetime.now() + datetime.timedelta(
            seconds=self.location_info.weather.offset_seconds
        )
        return render_time.strftime("%X, %x")

    async def _format_visibility(self) -> str:
        """
        Форматирование информации о видимости.
        Необходимо преобразовать ответ из метров в километры.

        :return:
        """

        # pylint: disable=C0209
        return f"{self.location_info.weather.visibility / 1000}"

    async def _format_languages(self) -> str:
        """
        Форматирование информации о языках.

        :return:
        """

        return ", ".join(
            f"{item.name} ({item.native_name})"
            for item in self.location_info.location.languages
        )

    async def _format_area(self) -> str:
        """
        Форматирование информации о площади.

        :return:
        """

        # pylint: disable=C0209

        if self.location_info.location.area is None:
            return "Нет информации о"

        return "{:,.0f}".format(self.location_info.location.area).replace(",", ".")

    async def _format_population(self) -> str:
        """
        Форматирование информации о населении.

        :return:
        """

        # pylint: disable=C0209
        return "{:,}".format(self.location_info.location.population).replace(",", ".")

    async def _format_currency_rates(self) -> str:
        """
        Форматирование информации о курсах валют.

        :return:
        """

        return ", ".join(
            f"{currency} = {Decimal(rates).quantize(exp=Decimal('.01'), rounding=ROUND_HALF_UP)} руб."
            for currency, rates in self.location_info.currency_rates.items()
        )
