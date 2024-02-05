import mysql.connector
import json

def connect_to_database():
    # Connect to MySQL database
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )

def fetch_data_from_mysql(cursor, table_name):
    # Example: Fetch data from MySQL and convert to JSON
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()

    # Convert MySQL result to JSON
    json_data = json.dumps(result, default=str)
    return json_data

def insert_json_into_mysql(cursor, json_data):
    # Example: Insert JSON data into MySQL
    query_insert = "INSERT INTO your_table (json_column) VALUES (%s)"
    cursor.execute(query_insert, (json_data,))

    # Commit the changes
    conn.commit()

def close_connection(cursor, conn):
    # Close the cursor and connection
    cursor.close()
    conn.close()

# Main program
conn = connect_to_database()
cursor = conn.cursor()

# Fetch data from MySQL
json_data_result = fetch_data_from_mysql(cursor)
print("Fetched JSON Data:", json_data_result)

# Insert JSON data into MySQL
json_data_to_insert = '{"key": "value"}'
insert_json_into_mysql(cursor, json_data_to_insert)
print("Inserted JSON Data into MySQL.")

# Close the cursor and connection
close_connection(cursor, conn)


# import mysql.connector
# from mysql.connector import Error
# import sys
# import http.server
# import socketserver

# def connect_to_database():
#     try:
#         connection = mysql.connector.connect(
#             host='mysql687.loopia.se',
#             database='smrcak_rs_db_2',
#             user='dejan@s70660',
#             password='base2024'
#         )
#         if connection.is_connected():
#             print("Connected to the database")
#             return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# def close_connection(connection):
#     if connection.is_connected():
#         connection.close()
#         print("Connection closed")

# def list_words(connection):
#     cursor = connection.cursor()
#     try:
#         query = "SELECT * FROM words"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         return results
#         # for result in results:
#         #     print(result)
#     except Error as e:
#         print(f"Error listing words: {e}")
#         return []
#     finally:
#         cursor.close()

# def add_word(connection, word, meaning):
#     cursor = connection.cursor()
#     try:
#         query = "INSERT INTO words (word, meaning) VALUES (%s, %s)"
#         cursor.execute(query, (word, meaning))
#         connection.commit()
#         print("Word added successfully")
#     except Error as e:
#         print(f"Error adding word: {e}")
#     finally:
#         cursor.close()
#         connection.close()

# def delete_word(connection, word):
#     cursor = connection.cursor()
#     try:
#         query = "DELETE FROM words WHERE word = %s"
#         cursor.execute(query, (word,))
#         connection.commit()
#         print("Word deleted successfully")
#     except Error as e:
#         print(f"Error deleting word: {e}")
#     finally:
#         cursor.close()

# def edit_word(connection, old_word, new_word, new_meaning):
#     cursor = connection.cursor()
#     try:
#         query = "UPDATE words SET word = %s, meaning = %s WHERE word = %s"
#         cursor.execute(query, (new_word, new_meaning, old_word))
#         connection.commit()
#         print("Word edited successfully")
#     except Error as e:
#         print(f"Error editing word: {e}")
#     finally:
#         cursor.close()

# def generate_html(results):
#     with open('template.html', 'r', encoding="utf8") as template_file:
#         template_content = template_file.read()

#     rendered_content = template_content.replace('{% for result in results %}', '')
#     for result in results:
#         rendered_content += f"""
#         <li class='card' onmousedown="preventTextSelection(event)" ondblclick="rotateCard(this)">
#                 <p class='card-front'>{result[1]}</p>
#                 <p class='card-back'>back</p>
#             </li>
#         </ul>
#         <div class="meaning">
#             <p>{result[2]}</p>
#         """

#     rendered_content += template_content.replace('{% endfor %}', '')

#     with open('words_list.html', 'w', encoding="utf8") as html_file:
#         html_file.write(rendered_content)

#     print('HTML file generated: words_list.html')


# def serve_html_on_localhost():
#     PORT = 8000
#     Handler = http.server.SimpleHTTPRequestHandler

#     with socketserver.TCPServer(("", PORT), Handler) as httpd:
#         print(f"Serving on http://localhost:{PORT}/words_list.html")
        # httpd.serve_forever()

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: main.py <operation> <word> <meaning>")
#         sys.exit(1)

#     operation = sys.argv[1].lower()
#     if len(sys.argv) > 2:
#         word = sys.argv[2]
#         meaning = sys.argv[3]

#     connection = connect_to_database()

#     if connection:
#         try:
#             if operation == "list":
#                 list_words(connection)
#                 results = list_words(connection)
#                 generate_html(results)
#                 serve_html_on_localhost()
#             elif operation == "add":
#                 add_word(connection, word, meaning)
#             elif operation == "delete":
#                 delete_word(connection, word)
#             elif operation == "edit":
#                 if len(sys.argv) < 6:
#                     print("Usage for edit: main.py edit <old_word> <new_word> <new_meaning>")
#                     sys.exit(1)
#                 old_word = word
#                 new_word = sys.argv[4]
#                 new_meaning = sys.argv[5]
#                 edit_word(connection, old_word, new_word, new_meaning)
#             else:
#                 print("Invalid operation. Please choose add, delete, or edit.")
#         finally:
#             close_connection(connection)

# # Connect to the database
# conn = mysql.connector.connect(
#     host="mysql687.loopia.se",
#     user="dejan@s70660",
#     password="base2024",
#     database="smrcak_rs_db_2"
# )

# import mysql.connector
# from mysql.connector import Error
# import sys