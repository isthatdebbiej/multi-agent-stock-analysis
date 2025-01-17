import psycopg2
from utils.logger import get_logger

logger = get_logger("SQLStorage")

class SQLStorage:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()
        logger.info("Connected to PostgreSQL database")

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS stock_prices (
            id SERIAL PRIMARY KEY,
            stock_symbol VARCHAR(10),
            date DATE,
            open_price FLOAT,
            close_price FLOAT,
            volume BIGINT
        );
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()
        logger.info("Created stock_prices table")

    def insert_data(self, stock_data):
        insert_query = """
        INSERT INTO stock_prices (stock_symbol, date, open_price, close_price, volume)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.executemany(insert_query, stock_data)
        self.conn.commit()
        logger.info(f"Inserted {len(stock_data)} rows into stock_prices table")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        logger.info("Closed PostgreSQL connection")
