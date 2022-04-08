import mysql.connector


def authenticate(username, password):
    conn = mysql.connector.connect(host='34.142.45.84',
                               database='reymysterio',
                               user='root',
                               password='root437root')
    cursor = conn.cursor()

    cursor = conn.cursor()
    cursor.execute("select username from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) == 0:
        return 1  # incorrect username, username does not exist

    cursor.execute("select password from users WHERE username='"+str(username)+"'")
    res = cursor.fetchall()
    retPassword = res[0][0]
    if retPassword != password:
        return 2  # incorrect password
    return 0


def register(username, password):
    conn = mysql.connector.connect(host='34.142.45.84',
                               database='reymysterio',
                               user='root',
                               password='root437root')
    cursor = conn.cursor()

    cursor.execute("select username from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) != 0:
        return 1  # username already exists in database

    SQL = '''insert into users(username,password)
            values ('{}','{}')'''.format(username, password)
    cursor.execute(SQL)
    conn.commit()
    return 0



