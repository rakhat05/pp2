import psycopg2 as pgsql

connection = pgsql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name)
cur = connection.cursor()


def pagination():
    query = createpattern()
    if query == "error":
        return "error"
    print("Need offset? yes/no:")
    mode = input()
    if mode == "yes":
        print("Enter offset:")
        offset = int(input())
        query += " OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode = input()
    if mode == "yes":
        print("Enter limit:")
        limit = int(input())
        query += " LIMIT {}".format(limit)
    query += ";"
    return query
