from database_connection import get_database_connection

def drop_tables(connection):
    """

    Args:
        connection ([type]): [description]
    """

    cursor = connection.cursor()

    cursor.execute(''' DROP TABLE IF EXISTS calculations; ''')

    connection.commit()

def create_table(connection):
    """[summary]

    Args:
        connection ([type]): [description]
    """

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE calculations ( 
            expression text primary key,
            answer text
        );
    ''')

    connection.commit()

def initialize_database():
    """[summary]
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_table(connection)

if __name__ == "__main__":
    initialize_database()