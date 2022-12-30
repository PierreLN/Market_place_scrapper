from Market_place_scrapper.backend.model.object.product import Product
from Market_place_scrapper.backend.model.object.retailer import Retailer
import neo4j
import pymongo
from pymongo import MongoClient

class DAOConnection:
    class CredentialsData:
        def __init__(self) -> None:
            pass

    def __init__(self) -> None:
        self.driver: neo4j.GraphDatabase = None
        self.open_connection()

    def open_connection(self) -> bool:
        pass

    def close(self):
        pass

    def get_attibut(self, result: dict, attribute: str) -> any:
        pass

    def get_element(Self) -> any:
        pass

    def add_element(self, element: any) -> bool:
        pass

    def set_element(self, element: any) -> bool:
        pass

    def return_connection(self) -> any:
        pass

class ConnectionNeo4j(DAOConnection):
    class CredentialsData:
        def __init__(self) -> None:
            self.NEO4J_URI: str = ''
            self.NEO4J_USERNAME: str = ''
            self.NEO4J_PASSWORD: str = ''

    def __init__(self) -> None:
        super().__init__()

    def open_connection(self) -> None:
        uri = self.CredentialsData().NEO4J_URI
        user = self.CredentialsData().NEO4J_USERNAME
        password = self.CredentialsData().NEO4J_PASSWORD
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        self.driver.close()

    def get_attibut(self, result: dict, attribute: str) -> any:
        try:
            return result['n'][attribute]
        except TypeError:
            return None
    
    def return_connection(self) -> neo4j.GraphDatabase.driver:
        return self.driver


class ConnectionMongoDB(DAOConnection):
    class CredentialsData:
        def __init__(self) -> None:
            self.MONGODB_CONNECTION_STR: str = ''
            self.DATABASE_PROJET: str = ''
            self.DATABASE_PRODUCT: str = ''
            self.DATABASE_USER: str = ''
            self.DATABASE_RETAILER: str = ''

    def __init__(self) -> None:
        super().__init__()

    def open_connection(self) -> None:
        connection_str = self.CredentialsData().MONGODB_CONNECTION_STR
        database = self.CredentialsData().DATABASE_PROJET
        collection_product = self.CredentialsData().DATABASE_PRODUCT
        collection_user = self.CredentialsData().DATABASE_USER
        db = client[database]
        self.table_product = db[collection_product]
        self.table_user = db[collection_user]