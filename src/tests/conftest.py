"""
Фикстуры для моделей объектов.
"""
import pytest
from collectors.models import (
    NewsDTO,
    LocationDTO,
    LanguagesInfoDTO,
    CurrencyInfoDTO,
    CountryDTO,
    WeatherInfoDTO,
    NewsInfoDTO,
    LocationInfoDTO,
)


@pytest.fixture
def news_model_fixture() -> NewsDTO:
    """
    Фикстура модели страны для получения сведений о новостях.

    :return: NewsDTO
    """

    return NewsDTO(
        alpha2code="pl",
    )


@pytest.fixture
def location_model_fixture() -> LocationDTO:
    """
    Фикстура модели локации для получения сведений о погоде.

    :return: LocationDTO
    """

    return LocationDTO(
        capital="Warsaw",
        alpha2code="PL",
    )


@pytest.fixture
def location_info_model_fixture() -> LocationInfoDTO:
    """
    Фикстура модели данных для представления общей информации о месте.

    :return: LocationInfoDTO
    """

    return LocationInfoDTO(
        location=CountryDTO(
            capital="Mariehamn",
            capital_latitude=60.116667,
            capital_longitude=19.9,
            alpha2code="AX",
            alt_spellings=["AX", "Aaland", "Aland", "Ahvenanmaa"],
            currencies={
                CurrencyInfoDTO(
                    code="EUR",
                )
            },
            flag="http://assets.promptapi.com/flags/AX.svg",
            languages={LanguagesInfoDTO(name="Swedish", native_name="svenska")},
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
        news=[
            NewsInfoDTO(
                author="BBC News",
                title="What does the King's diagnosis mean for William, Harry and the other royals?",
                description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                "to bring them together?",
                url="https://www.bbc.co.uk/news/uk-68211941",
                publishedAt="2024-02-06T12:37:22Z",
            ),
            NewsInfoDTO(
                author="BBC News",
                title="What does the King's diagnosis mean for William, Harry and the other royals?",
                description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                "to bring them together?",
                url="https://www.bbc.co.uk/news/uk-68211941",
                publishedAt="2024-02-06T12:37:22Z",
            ),
            NewsInfoDTO(
                author="BBC News",
                title="What does the King's diagnosis mean for William, Harry and the other royals?",
                description="It's been a bleak midwinter for the Royal Family. Will the King's health news help"
                "to bring them together?",
                url="https://www.bbc.co.uk/news/uk-68211941",
                publishedAt="2024-02-06T12:37:22Z",
            ),
        ],
    )
