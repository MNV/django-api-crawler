from abc import ABC, abstractmethod


class ApiBase(ABC):
    """
    APIs base methods.
    """
    @abstractmethod
    def get_url(self) -> str:
        pass

    @abstractmethod
    def process_import(self) -> int:
        pass
