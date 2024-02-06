"""
Функции для формирования выходной информации.
"""

import datetime
from decimal import ROUND_HALF_UP, Decimal

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

    async def render(self) -> tuple[str, ...]:
        """
        Форматирование прочитанных данных.

        :return: Результат форматирования
        """

        return (
            f"Страна: {self.location_info.location.name}",
            f"Столица: {self.location_info.location.capital}",
            f"Широта столицы: {self.location_info.location.capital_latitude}",
            f"Долгота столицы: {self.location_info.location.capital_longitude}",
            f"Часовой пояс столицы: {await self._get_timezone()}",
            f"Площадь: {await self._format_area()} км²",
            f"Регион: {self.location_info.location.subregion}",
            f"Языки: {await self._format_languages()}",
            f"Население страны: {await self._format_population()} чел.",
            f"Курсы валют: {await self._format_currency_rates()}",
            "-----------------погода в столице---------------------------",
            f"Сейчас в {self.location_info.location.capital} {await self._format_current_time()}",
            f"Температура: {self.location_info.weather.temp} °C",
            f"Погода: {self.location_info.weather.description}",
            f"Влажность: {self.location_info.weather.humidity}%",
            f"Видимость: {await self._format_visibility()} км",
            f"Скорость ветра: {self.location_info.weather.wind_speed} м/с",
        )

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
        dt = datetime.datetime.now() + datetime.timedelta(
            seconds=self.location_info.weather.offset_seconds
        )
        return dt.strftime("%X, %x")

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
        else:
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
