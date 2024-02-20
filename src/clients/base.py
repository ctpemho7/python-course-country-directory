"""
Базовые функции для клиентов внешних сервисов.
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseClient(ABC):
    """
    Базовый класс, реализующий интерфейс для клиентов.
    """

    @abstractmethod
    async def get_base_url(self) -> str:
        """
        Получение базового URL для запросов.

        :return: url в str-формате
        """

    @abstractmethod
    async def _request(self, endpoint: str) -> Optional[dict]:
        """
        Формирование и выполнение запроса.

        :param endpoint: Зндпоинт, куда отправляется запрос
        :return: ответ от API в формате dict
        """
