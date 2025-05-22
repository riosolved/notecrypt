from flask import jsonify
import mariadb

class Database:
    def __init__(self):
        self.connection = None

    def initialize(
        self,
        configuration
    ):
        try:
            print(f"""[DATABASE][Connection] Connecting with user: {
                configuration['user']
            }, host: {
                configuration['host']
            }, database: {
                configuration['database']
            }, port: {
                int(configuration['port'])
            }""")

            self.connection = mariadb.connect(
                user=configuration['user'],
                password=configuration['password'],
                host=configuration['host'],
                port=int(configuration['port']),
                database=configuration['database']
            )
        except mariadb.Error as error:
            print(f"[DATABASE][Connection] Error: {error}")

            raise RuntimeError("Issue initializing database")

    def instance(self):
        if self.connection is None:
            raise RuntimeError("Database not initialized")

        try:
            return {
                "connection": self.connection,
                "cursor": self.connection.cursor(),
            }
        except mariadb.Error as error:
            print(f"[DATABASE][Instance] Error: {error}")

            raise RuntimeError("Unable to interface with database")

database = Database()