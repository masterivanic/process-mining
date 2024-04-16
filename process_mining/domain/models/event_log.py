from typing import Any
from typing import Dict


class EventLog:
    EVENT_LOG_ATTRIBUTES = ["case_id", "activity", "timestamp", "ressource"]

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.__dict__.update(kwargs)
        attributes = list(self.__dict__.keys())
        for attr in self.EVENT_LOG_ATTRIBUTES:
            if attr not in attributes:
                raise AttributeError(f"{attr} not found, ['case_id', 'activity', 'timestamp', 'ressource'] \
                                     fields must contains in entry log")

    @classmethod
    def event_log(cls, **kwargs) -> "EventLog":
        event_class = super(EventLog, cls).__new__(cls)
        return event_class


def event_log_factoy(**kwargs) -> EventLog:
    return EventLog(**kwargs)
