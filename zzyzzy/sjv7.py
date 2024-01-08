import sys
import oracledb

# 데이터베이스 연결정보
host = '15.165'
userid = ''
passwd = '' 
sid = 'FREE'

dsn_tns = oracledb.makedsn(host, 1521, sid)

# 메뉴 출력
def show_menu():
    """
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
    --------------------
    성적처리 프로그램 v7
    --------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    --------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 성적 데이터 입력받음
def read_sungjuk():
    """
    성적 데이터 입력받음
    :return:
    """
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 88 99) : ')
    data = sungjuk.split()   # 빈칸으로 문자열 분리
    
    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    mat = int(data[3])
    sj = [name, kor, eng, mat]   # 입력받은 성적데이터를 리스트에 담음
    
    return sj


# 성적 처리 (총점/평균/학점 계산)
def compute_sungjuk(sj):
    """
    성적 처리 (총점/평균/학점 계산)
    :param sj: 입력된 성적데이터
    :return: 성적처리된 성적데이터
    """
    tot = sj[1] + sj[2] + sj[3]
    avg = float(f"{tot / 3:.1f}")
    grd = '수' if avg >= 90 else \
        '우' if avg >= 80 else \
            '미' if avg >= 70 else \
                '양' if avg >= 60 else '가'

    return [sj[0], sj[1], sj[2], sj[3], tot, avg, grd]


# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """
    모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
    :return:
    """
    print('성적데이터 조회')

    sql = ' select sjno, name, kor, eng, mat, regdate from sungjuk' \
          ' order by sjno desc '
    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql)

    for sjno, name, kor, eng, mat, regdate in cursor:
        print(sjno, name, kor, eng, mat, str(regdate)[:10])

    cursor.close()
    conn.close()


# 성적 데이터 저장 (sungjuk 테이블)
def save_sungjuk(sj):
    """
    성적 데이터 저장 (sungjuk 테이블)
    :param sj: 입력받아 처리된 성적데이터
    :return:
    """
    sql = ' insert into sungjuk (name, kor, eng, mat, tot, avg, grd) '\
          ' values (:1,:2,:3,:4, :5,:6,:7) '
          # ' values (:name,:kor,:eng,:mat, :tot,:avg,:grd) '
          # ' values (?,?,?,?, ?,?,?) ' # 오라클 x

    conn = oracledb.connect(
            user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql, sj)
    conn.commit()
    print(cursor.rowcount, '건의 성적데이터 추가됨!')

    cursor.close()
    conn.close()


# 성적 데이터 추가 (입력-처리-저장)
def addsungjuk():
    """
    성적 데이터 추가 (입력-처리-저장)
    :return: 
    """
    print('성적데이터 추가')
    sj = read_sungjuk()
    sj = compute_sungjuk(sj)
    save_sungjuk(sj)   # 성적데이터를 파일에 저장


# 성적 데이터 상세 조회
def showone_sungjuk():
    """
    성적 데이터 상세 조회
    :return: 
    """
    sjno = input('상세 조회할 학생번호는?')

    sql = ' select * from sungjuk where sjno = :1 '
    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql, [sjno])

    for sjno, name, kor, eng, mat, tot, avg, grd, regdate in cursor:
        print(sjno, name, kor, eng, mat, tot, avg, grd, regdate)

    cursor.close()
    conn.close()


    info = '찾는 데이터가 없어요!!'


# 성적 데이터 수정시 수정할 데이터 입력받기
def read_again(sjno):
    """
    성적 데이터 수정시 수정할 데이터 입력받는 함수
    :param sjno: 수정할 학생번호
    :return: 새롭게 생성된 성적데이터
    """
    sql = ' select name, kor, eng, mat from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql, [sjno])

    sj = [None, None, None, None]
    for name, kor, eng, mat in cursor:
        sj = [name, kor, eng, mat]

    cursor.close()
    conn.close()

    if sj[0]:  # 만일, 수정할 데이터가 존재한다면
        sj[0] = input(f'새로운 이름은? ({sj[0]}) : ')
        sj[1] = int(input(f'새로운 국어는? ({sj[1]}) : '))
        sj[2] = int(input(f'새로운 영어는? ({sj[2]}) : '))
        sj[3] = int(input(f'새로운 수학은? ({sj[3]}) : '))
        sj = compute_sungjuk(sj)

    return sj


# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return:
    """
    sjno = input('수정할 학생번호는?')

    # 수정할 성적데이터를 입력받고 성적처리한 결과를 받아옴
    sj = read_again(sjno)

    if sj[0]: # 수정할 데이터를 찾았다면
        sql = ' update sungjuk set name=:1, kor=:2, eng=:3, '\
              ' mat=:4, tot=:5, avg=:6, grd=:7, regdate=sysdate '\
              ' where sjno=:8 '
        sj.append(sjno)

        conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
        cursor = conn.cursor()

        cursor.execute(sql, sj)
        conn.commit()
        print(f'{cursor.rowcount} 건의 데이터가 수정되었습니다!')

        cursor.close()
        conn.close()
    else:
        print('찾는 데이터가 없습니다!')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터 삭제
    :return:
    """
    sjno = input('삭제할 학생번호는?')
    sql = ' delete from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql, [sjno])
    conn.commit()
    print(f'{cursor.rowcount} 건의 데이터가 삭제되었습니다!')

    cursor.close()
    conn.close()


# 성적처리 프로그램 종료
def exit_program():
    """
    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
