import psycopg2 as pgsql

connection = pgsql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name)
cur = connection.cursor()


def delete():
    query = """DELETE FROM phonebook
    WHERE """
    cur.execute("SELECT * from phonebook")
    print(cur.fetchall())
    print("Do you wanna delete by last_name(0)/first_name(1)/phone_num(2) enter the number")
    mode = int(input())
    if mode == 0:
        print("Enter last_name to delete:")
        last_name = input()
        query += "last_name='{}'".format(last_name)
    elif mode == 1:
        print("Enter first_name to delete:")
        first_name = input()
        query += "first_name='{}'".format(first_name)
    else:
        print("Enter phone_num to delete:")
        phone_num = input()
        query += "phone_num={}".format(phone_num)
    cur.execute(query)


s1 = createpattern()
if s1 != "error":
    cur.execute(s1+";")
    print(cur.fetchall())
insert("Berik", "Serik", 123)
loopinsert()
s1 = pagination()
if s1 != "error":
    cur.execute(s1+";")
    print(cur.fetchall())
delete()

connection.commit()
cur.close()
connection.close()
