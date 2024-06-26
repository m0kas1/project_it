import sqlite3

def starting_id_name(user: int, name: str):
    db = sqlite3.connect('m0kas1.db')
    c = db.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS piple (
        user_id INTEGER UNIQUE,
        username TEXT,
        factory TEXT
    
    )''')

    # user = int(input())
    # name = input()

    c.execute(f"SELECT * FROM piple WHERE user_id = {user}")
    all = c.fetchone()
    print(all)
    if all:
        print("Такой пользователь уже есть!")
    else:
        c.execute("INSERT INTO piple (user_id, username, factory) VALUES (?, ?, ?)", (user, f"{name}", '0'))
        db.commit()
        c.execute(f"SELECT * FROM piple WHERE user_id = {user}")
        k = c.fetchone()
        print(k)

    db.commit()
    db.close()
# c.execute("INSERT INTO piple (user_id, username) VALUES (23132152315, 'mix')")
# c.execute("INSERT INTO piple VALUES (32463246, 'anton', 'gres')")

# c.execute('DELETE FROM piple WHERE username = "m0kas1"')

# c.execute("SELECT * FROM piple")
# items = c.fetchall()
# print(items)
# print(c.fetchmany(1))
# print(c.fetchone())
# for i in items:
#     print(i[])