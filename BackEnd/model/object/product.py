
from datetime import date
class Product:
    def __init__(self):
        self.__id: int = None
        self.__name: str = None
        self.__price: float = None
        self.__date: date = None
        self.__quantity = None
        self.__measure_unit = None
        self.__hyperlink = None
        self.__score = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int) -> int:
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> str:
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float) -> float:
        self.__price = value

    @property
    def date(self):
        return self.__date 

    @date.setter
    def date(self, value: date) -> date:
        self.__date = value

    @property
    def quantity(self) -> float:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float) -> float:
        self.__quantity = value

    @property
    def measure_unit(self) -> str:
        return self.__measure_unit

    @measure_unit.setter
    def measure_unit(self, value: str) -> str:
        self.__measure_unit = value

    @property
    def hyperlink(self) -> str:
        return self.__hyperlink

    @hyperlink.setter
    def hyperlink(self) -> str:
        self.__hyperlink = value

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, value: int) -> int:
        self.__score = value