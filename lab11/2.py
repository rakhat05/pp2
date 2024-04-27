import psycopg2 as pgsql

connection = pgsql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name)
cur = connection.cursor()


def insert(last_name, first_name, phone_num):
    cur.execute(
        "SELECT count(*) FROM phonebook WHERE last_name='{}' AND first_name='{}'".format(last_name, first_name))
    if cur.fetchone()[0] == 0:
        cur.execute("""INSERT INTO phonebook VALUES ('{}','{}', {})""".format(
            last_name, first_name, phone_num))
    else:
        cur.execute("""UPDATE phonebook
         SET number={}
         WHERE last_name='{}' AND first_name='{}'
         """.format(phone_num, last_name, first_name))
