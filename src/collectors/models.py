"""
Описание моделей данных (DTO).
"""
from typing import Optional

from pydantic import Field, BaseModel


class HashableBaseModel(BaseModel):
    """
    Добавление хэшируемости для моделей.
    """

    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class NewsDTO(HashableBaseModel):
    """
    Модель страны для получения сведений о новостях.

    .. code-block::

        NewsDTO(
            alpha2code="ru",
        )
    """

    alpha2code: str = Field(min_length=2, max_length=2)  # country alpha‑2 code


class LocationDTO(HashableBaseModel):
    """
    Модель локации для получения сведений о погоде.

    .. code-block::

        LocationDTO(
            capital="Mariehamn",
            alpha2code="AX",
        )
    """

    capital: str
    alpha2code: str = Field(min_length=2, max_length=2)  # country alpha‑2 code


class CurrencyInfoDTO(HashableBaseModel):
    """
    Модель данных о валюте.

    .. code-block::

        CurrencyInfoDTO(
            code="EUR",
        )
    """

    code: str


class LanguagesInfoDTO(HashableBaseModel):
    """
    Модель данных о языке.

    .. code-block::

        LanguagesInfoDTO(
            name="Swedish",
            native_name="svenska"
        )
    """

    name: str
    native_name: str


class CountryDTO(BaseModel):
    """
    Модель данных о стране.

    .. code-block::

        CountryDTO(
            capital="Mariehamn",
            capital_latitude=60.116667,
            capital_longitude=19.9,
            alpha2code="AX",
            alt_spellings=[
              "AX",
              "Aaland",
              "Aland",
              "Ahvenanmaa"
            ],
            currencies={
                CurrencyInfoDTO(
                    code="EUR",
                )
            },
            flag="http://assets.promptapi.com/flags/AX.svg",
            languages={
                LanguagesInfoDTO(
                    name="Swedish",
                    native_name="svenska"
                )
            },
            name="\u00c5land Islands",
            population=28875,
            subregion="Northern Europe",
            timezones=[
                "UTC+02:00",
            ],
        )
    """

    capital: str
    capital_latitude: float
    capital_longitude: float
    alpha2code: str
    alt_spellings: list[str]
    currencies: set[CurrencyInfoDTO]
    flag: str
    languages: set[LanguagesInfoDTO]
    name: str
    population: int
    area: Optional[float]
    subregion: str
    timezones: list[str]


class CurrencyRatesDTO(BaseModel):
    """
    Модель данных о курсах валют.

    .. code-block::

        CurrencyRatesDTO(
            base="RUB",
            date="2022-09-14",
            rates={
                "EUR": 0.016503,
            }
        )
    """

    base: str
    date: str
    rates: dict[str, float]


class WeatherInfoDTO(BaseModel):
    """
    Модель данных о погоде.

    .. code-block::

        WeatherInfoDTO(
            temp=13.92,
            pressure=1023,
            humidity=54,
            visibility=10_000,
            wind_speed=4.63,
            description="scattered clouds",
            offset_seconds=3600,
        )
    """

    temp: float
    pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    description: str
    offset_seconds: int


class NewsInfoDTO(BaseModel):
    """
    Модель данных о новостях.

    .. code-block::

        NewsInfoDTO(
            author="BBC News",
            title="What does the King's diagnosis mean for William, Harry and the other royals?",
            description="It's been a bleak midwinter for the Royal Family. Will the King's health news help to bring"
            "them together?",
            url="https://www.bbc.co.uk/news/uk-68211941",
            published_at="2024-02-06T12:37:22Z",
        )
    """

    author: str
    title: str
    description: Optional[str]
    url: str
    published_at: str


class LocationInfoDTO(BaseModel):
    """
    Модель данных для представления общей информации о месте.

    .. code-block::

        LocationInfoDTO(
            location=CountryDTO(
                capital="Mariehamn",
                capital_latitude=60.116667,
                capital_longitude=19.9,
                alpha2code="AX",
                alt_spellings=[
                  "AX",
                  "Aaland",
                  "Aland",
                  "Ahvenanmaa"
                ],
                currencies={
                    CurrencyInfoDTO(
                        code="EUR",
                    )
                },
                flag="http://assets.promptapi.com/flags/AX.svg",
                languages={
                    LanguagesInfoDTO(
                        name="Swedish",
                        native_name="svenska"
                    )
                },
                name="\u00c5land Islands",
                population=28875,
                subregion="Northern Europe",
                timezones=[
                    "UTC+02:00",
                ],
            ),
            weather=WeatherInfoDTO(
                temp=13.92,
                pressure=1023,
                humidity=54,
                visibility=10_000,
                wind_speed=4.63,
                description="scattered clouds",
                offset_seconds=3600,
            ),
            currency_rates={
                "EUR": 0.016503,
            },
            news = [
                NewsInfoDTO(
                    author="BBC News",
                    title="What does the King's diagnosis mean for William, Harry and the other royals?",
                    description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                    "to bring them together?",
                    url="https://www.bbc.co.uk/news/uk-68211941",
                    published_at="2024-02-06T12:37:22Z",
                ),
                NewsInfoDTO(
                    author="BBC News",
                    title="What does the King's diagnosis mean for William, Harry and the other royals?",
                    description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                    "to bring them together?",
                    url="https://www.bbc.co.uk/news/uk-68211941",
                    published_at="2024-02-06T12:37:22Z",
                ),
                NewsInfoDTO(
                    author="BBC News",
                    title="What does the King's diagnosis mean for William, Harry and the other royals?",
                    description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                    "to bring them together?",
                    url="https://www.bbc.co.uk/news/uk-68211941",
                    published_at="2024-02-06T12:37:22Z",
                ),
            ]
        )
    """

    location: CountryDTO
    weather: WeatherInfoDTO
    news: list[NewsInfoDTO]
    currency_rates: dict[str, float]
