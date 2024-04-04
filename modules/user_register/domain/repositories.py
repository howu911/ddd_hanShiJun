from abc import ABC, abstractmethod

from seedwork.domain.entities import Entity


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: Entity):
        raise NotImplementedError


class SalesRepRepository(ABC):
    @abstractmethod
    def find(self, area_code: str, operator_code: str):
        raise NotImplementedError

