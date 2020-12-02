import sqlite3


def create(conn, cur):
    # 创建数据表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            tel VARCHAR,
            addr VARCHAR
        );
    """)
    conn.commit()


def show(conn, cur):
    cur.execute("""
        SELECT * FROM student;
    """)
    result = cur.fetchall()
    for item in result:
        print(item)


def append(conn, cur, data):
    cur.execute("""
        INSERT INTO student VALUES(?,?,?,?)
    """, (data['no'], data['name'], data['tel'], data['addr']))
    conn.commit()
    show(conn, cur)


def remove(conn, cur, no):
    cur.execute('DELETE FROM student WHERE id = {}'.format(no))
    conn.commit()
    show(conn, cur)


if __name__ == '__main__':

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    create(conn, cur)

    functionList = ['1', '2', '3']
    functionId = ''
    print("-------------功能列表-----------")
    print("1. 显示所有信息")
    print("2. 追加信息")
    print("3. 删除信息")

    while True:

        functionId = input("请输入数字1-3选择功能: ")

        if functionId not in functionList[:]:
            print("输入有误，请重新输入！")
            continue
        else:
            print("您选择了功能{}".format(functionId))
            break

    # 功能1.显示
    if functionId == functionList[0]:
        show(conn, cur)


    # 功能2.追加
    elif functionId == functionList[1]:
        dct = {}
        info = input('添加学生信息(格式, 逗号分隔 - 学号,姓名,电话,地址):').split(',')
        dct['no'] = info[0]
        dct['name'] = info[1]
        dct['tel'] = info[2]
        dct['addr'] = info[3]

        append(conn, cur, dct)

    # 功能3.删除
    elif functionId == functionList[2]:
        no = input('输入要删除的学号:')
        remove(conn, cur, no)




