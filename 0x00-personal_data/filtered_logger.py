#!/usr/bin/env python3
""" Module for filtered logger """
import logging
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """ Function to log filtered data """
    return re.sub(
        f"({'|'.join(fields)})=.*?{separator}",
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialization method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format for the message """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Get logger function """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logging.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Implement db conectivity """
    psw = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(
        host=host,
        database=db_name,
        user=username,
        password=psw)
    return conn


def main() -> None:
    """ Implement a main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " +\
            f"ssn={row[3]}; password={row[4]};ip={row[5]}; " +\
            f"last_login={row[6]}; user_agent={row[7]};"
        print(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
