from typing import Any
from abc import abstractmethod
from pydantic import BaseModel


class DataPipe(BaseModel):
    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @abstractmethod
    def store(self, data) -> str:
        """

        Args:
            data (Any): The data to be stored.
        Return:
            str: The name of the stored data.

        """

    @abstractmethod
    def retrieve(self, key) -> Any:
        """

        Args:
            key (Any): The key to identify the data.
        Return:
            Any: The retrieved data.

        """
