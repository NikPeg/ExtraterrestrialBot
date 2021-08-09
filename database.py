import sqlite3

con = sqlite3.connect('reload.db')
cur = con.cursor()

# cur.execute("CREATE TABLE character(id int AUTO_INCREMENT, name text, age int, description text, personality text, "
#             "marriage text, post text, country text)")
cur.execute("INSERT INTO character VALUES (1,'Дик Уэлдон XVI',34,'Наследник древнего "
            "рода Диков Уэлдонов. Честно продолжает политику Уэлдона I: всегда врёт и делает всё самое смешное и "
            "сумасшедшее, что можно придумать.','Весёлый и лживый','Не женат','Несменный ДИКтатор Хуан-Фернандеса',"
            "'Хуан-Фернандес')")
con.commit()
con.close()
