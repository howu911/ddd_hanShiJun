import uuid

from pydantic.dataclasses import dataclass


class GenericUUID(uuid.UUID):
    @classmethod
    def next_id(cls):
        return cls(int=uuid.uuid4().int)


@dataclass(frozen=True)
class ValueObject:
    """
    Base class for value objects
    """
