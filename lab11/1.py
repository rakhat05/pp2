import psycopg2 as pgsql

connection = pgsql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name)
cur = connection.cursor()


def createpattern():
    global query
    query = """SELECT * FROM phonebook
    WHERE """
    print(r"Do you want to search by first_name(0)/last_name(1)/break(any num) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "last_name"
        print("Enter string")
        substr = input()
        print("""Select option:
            1-last_name is equal to string
            2-last_name starts with the string
            3-last_name ends with the string
            4-last_name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    elif mode == 1:
        query += """first_name"""
        print("Enter string")
        substr = input()
        print("""Select option:
            1-first_name is equal to string
            2-first_name starts with the string
            3-first_name ends with the string
            4-first_name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    else:
        return "error"
    return query
