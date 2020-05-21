import sqlite3

# def add_name(database_file, new_person):
#     query = "INSERT INTO Person (id, personal, family) VALUES (?, ?, ?);"

#     connection = sqlite3.connect(database_file)
#     cursor = connection.cursor()
#     cursor.execute(query, list(new_person))
#     cursor.close()
#     connection.commit()
#     connection.close()


def get_name(req):
    query = "SELECT res FROM message WHERE req=?;"

    connection = sqlite3.connect("chatbotdb.sqlite")
    cursor = connection.cursor()
    cursor.execute(query, [req])
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results[0][0]

# # Insert a new name
# add_name('survey.db', ('barrett', 'Mary', 'Barrett'))
# # Check it exists
# print(get_name('chatbotdb.sqlite', 'hello'))