# TEST.ORACLE.PY
import cx_Oracle
import os
import crawling

location = "C:\instantclient_21_3"
os.environ["PATH"] = location + ";" + os.environ["PATH"]
cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_3")
conn = cx_Oracle.connect("c##student/student@192.168.219.108:1521/xe")


def intro():
    conn = cx_Oracle.connect("c##student/student@192.168.219.108:1521/xe")
    sql = "insert into covid values (null, null, null, null,null,null,null,null,null,null, null,sysdate);"
    cs = conn.cursor()
    return cs.execute(sql)

def database():

    list = crawling.seoul()
    seoul_num =list[0][0][0]
    korea_num = list[0][1][0]

    tuple_seoul_num = tuple(seoul_num)
    tuple_korea_num = tuple(korea_num)

    date = str(list[1][0])
    print(date)
    date=date[3:11]
    characters = "."
    date = ''.join(x for x in date if x not in characters)
    date = date[:2] +'/' + date[2:4] + '/' + date[4:]
    print(date)
    tp_date = (date, )
    tuple_result = tuple_seoul_num + tuple_korea_num + tp_date
    query = "INSERT INTO COVID VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
    cursor = conn.cursor()
    def to_db():
        sysdate = """
                        SELECT COVID_DATE
                        FROM COVID
                        """
        conn = cx_Oracle.connect('c##student/student@192.168.219.108:1521/xe')
        cs = conn.cursor()
        rs = cs.execute(sysdate)
        col1=[]
        for record in rs:
            col1.append(record[0])
            date_now=str(col1[0])
            global realdate
            realdate = date_now[2:4] +'/' + date_now[5:7] + '/' + date_now[8:10]
        return realdate

    # cursor.execute(query, tuple_result)
    if to_db() == date:
        pass
    else:
        cursor.execute(query, tuple_result)
    cursor.close()
    conn.commit()
    conn.close()

database()



