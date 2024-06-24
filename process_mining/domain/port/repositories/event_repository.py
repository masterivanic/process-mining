from abc import ABCMeta
from abc import abstractmethod
from typing import List
from typing import Type

from process_mining.domain.models.event_log import EventLog


class EventLogRepository(metaclass=ABCMeta):
    @abstractmethod
    def all(self) -> List[EventLog]: ...

    @abstractmethod
    def delete(self, event_id: Type[str | int]) -> None: ...
