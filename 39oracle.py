# 오라클디비로 데이터 다루기 1 - select
# cx_Oracle 모듈을 먼저 설치해야 함 - pip install cx_Oracle

# 1) Oracle instant client 버젼에 따라 VS 재배포 패키지 설치
# 2) Oracle instant client를 다운로드하고, c:/Java에 압축해제
# 3) Oracle instant client 설치경로를 시스템의 PATH 환경변수에 등록
# 4) 그런 다음, IntelliJ IDE를 다시 시작

# For Instant Client 21 install VS 2019 or later.
# For Instant Client 19 install VS 2017.
# https://www.oracle.com/kr/database/technologies/instant-client/downloads.html

# intelliJ에서 오라클 디비서버로 csv 파일 가져오기시
# 텍스트 컬럼은 자동으로 CLOB 타입으로 설정
# CLOB가 꼭 필요한 컬럼을 제외하고 varchar 타입으로 바꿀 것을 추천!!

import cx_Oracle

host = '15.165'
userid = ''
passwd = ''
sid = 'FREE'

# 디비 서버에 연결
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = 'select first_name, last_name from employees'
cursor.execute(sql)

for fname, lname in cursor:
     print(fname, lname)

cursor.close()
conn.close()


# 국가별 메달별 획득수 조회
# dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)
#
# cursor = conn.cursor()
#
# sql = ' select COUNTRY, MEDAL, count(COUNTRY) cnt '\
#       ' from SUMMERMEDALS2 group by COUNTRY, MEDAL '
# cursor.execute(sql)
#
# for country, medal, cnt in cursor:
#      print(country, medal, cnt)
#
# cursor.close()
# conn.close()


# 승선위치별(embark_town) 성별(sex) 생존자수(alive) 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = ' select EMBARK_TOWN, SEX, count(ALIVE) alives from TITANIC2 '\
      " where ALIVE = 'yes' group by EMBARK_TOWN, SEX "\
      ' order by EMBARK_TOWN, SEX '
cursor.execute(sql)

for embark, sex, alives in cursor:
     print(embark, sex, alives)

cursor.close()
conn.close()


# 승선위치별(embark_town) 사람별(who) 생존자수(alive) 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = 'select EMBARK_TOWN, WHO, count(WHO) alives from TITANIC2 '\
      ' group by EMBARK_TOWN, WHO order by EMBARK_TOWN, WHO '
cursor.execute(sql)

for embark, who, alives in cursor:
     print(embark, who, alives)

cursor.close()
conn.close()








