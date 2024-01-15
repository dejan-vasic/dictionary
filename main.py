import mysql.connector
from mysql.connector import Error
import sys

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")

def add_word(connection, word, meaning):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO words (word, meaning) VALUES (%s, %s)"
        cursor.execute(query, (word, meaning))
        connection.commit()
        print("Word added successfully")
    except Error as e:
        print(f"Error adding word: {e}")
    finally:
        cursor.close()

def delete_word(connection, word):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM words WHERE word = %s"
        cursor.execute(query, (word,))
        connection.commit()
        print("Word deleted successfully")
    except Error as e:
        print(f"Error deleting word: {e}")
    finally:
        cursor.close()

def edit_word(connection, old_word, new_word, new_meaning):
    cursor = connection.cursor()
    try:
        query = "UPDATE words SET word = %s, meaning = %s WHERE word = %s"
        cursor.execute(query, (new_word, new_meaning, old_word))
        connection.commit()
        print("Word edited successfully")
    except Error as e:
        print(f"Error editing word: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: main.py <operation> <word> <meaning>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    word = sys.argv[2]
    meaning = sys.argv[3]

    connection = connect_to_database()

    if connection:
        try:
            if operation == "add":
                add_word(connection, word, meaning)
            elif operation == "delete":
                delete_word(connection, word)
            elif operation == "edit":
                if len(sys.argv) < 6:
                    print("Usage for edit: main.py edit <old_word> <new_word> <new_meaning>")
                    sys.exit(1)
                old_word = word
                new_word = sys.argv[4]
                new_meaning = sys.argv[5]
                edit_word(connection, old_word, new_word, new_meaning)
            else:
                print("Invalid operation. Please choose add, delete, or edit.")
        finally:
            close_connection(connection)

# Connect to the database
conn = mysql.connector.connect(
    host="mysql687.loopia.se",
    user="dejan@s70660",
    password="base2024",
    database="smrcak_rs_db_2"
)


