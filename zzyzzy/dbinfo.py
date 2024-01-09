import oracledb
import pymysql
import os

# 시스템 환경변수 등록
# linux : export 키=값
# window : set 키=값

url = os.getenv('URL')
userid = os.getenv('USR')
passwd = os.getenv('PWD')
dbname = os.getenv('DBN')
sid = os.getenv('SID')
dsn_tns = oracledb.makedsn(url, 1521, sid)


def openConn():
    """
    데이터베이스 커서와 커넥션 객체 생성
    :return: 커서, 커넥션 객체 반환
    """
    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cur = conn.cursor()

    return cur, conn


def closeConn(cur, conn):
    """
    데이터베이스 커서와 연결 종료
    :param cur: 접속중인 커서 객체
    :param conn: 접속중인 커넥션 객체
    :return: 없음
    """
    cur.close()
    conn.close()

