# import json_data  # Import the JSON data from the separate file
# import sqlite3
#
# def create_table_from_json(json_data):
#     columns = []
#     for key, value in json_data.items():
#         if isinstance(value, int):
#             column_type = 'INTEGER'
#         elif isinstance(value, float):
#             column_type = 'REAL'
#         elif isinstance(value, bool):
#             column_type = 'INTEGER'  # SQLite does not have a dedicated boolean type, so we use INTEGER (0 for False, 1 for True)
#         else:
#             column_type = 'TEXT'
#         columns.append(f"{key} {column_type}")
#
#     create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});"
#     cursor.execute(create_table_query)
#
# # Access the JSON data from the imported module
# json_data = json_data.data
#
# # Create SQLite database or connect to an existing one
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
#
# for table_name, table_data in json_data.items():
#     create_table_from_json(table_data)
#
# # Commit changes and close the connection
# conn.commit()
# conn.close()
