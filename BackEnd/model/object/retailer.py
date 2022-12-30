from datetime import date

class Retailer:
    def __init__(self):
        self.__name = None
        self.__hyperlink = None
        self.__address = None

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> bool:
        self.__name = value

    @property
    def hyerlink(self) -> str:
        return self.__hyperlink

    @hyperlink.setter
    def hyperlink(self, value: str) -> bool:
        self.__hyperlink

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, vaule: str) -> bool:
        self.__address = value