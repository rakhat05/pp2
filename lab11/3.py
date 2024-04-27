import psycopg2 as pgsql

connection = pgsql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name)
cur = connection.cursor()


def loopinsert():
    banned = []
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input()
        if mode == "no":
            break
        person = input().split()
        if len(person) > 3:
            banned.append(person)
            continue

        if not person[2].isdigit():
            banned.append(person)
            continue

        insert(*person)
    if len(banned) == 0:
        return
    print("This data were not added due to incorrect format:")
    for i in banned:
        print(i)
