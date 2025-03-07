import database
conn = database.get_db()
sql_query = "select * from todo"
cursor = conn.cursor()
cursor.execute(sql_query)
result = cursor.fetchall()
todos = []  #list of dict
for col in result:
    todos.append({
                    "title" : col[0],
                    "descr" : col[1],
                    "status" : col[2]
    }) 
# print(todos)

