import sys
from zzyzzy.SungJuk import SungJuk
from zzyzzy.SungJukService import SungJukService
from zzyzzy.SungJukDAO import SungJukDAO


# 메뉴 출력
def show_menu():
    """
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
    --------------------
    성적처리 프로그램 v8
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


# 성적 데이터 추가 (입력-처리-저장)
def addsungjuk():
    """
    성적 데이터 추가 (입력-처리-저장)
    :return: 
    """
    print('성적데이터 추가')

    sj = SungJukService.read_sungjuk()
    SungJukService.compute_sungjuk(sj)

    rowcnt = SungJukDAO.insert_sungjuk(sj)

    print(f'{rowcnt} 건의 성적데이터 추가됨!!')


# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """
    모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
    :return:
    """
    print('성적데이터 조회')
    rows = SungJukDAO.select_sungjuk()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} '
              f'{row[4]} {str(row[5])[:10]}')


# 성적 데이터 상세 조회
def showone_sungjuk():
    """
    성적 데이터 상세 조회
    :return: 
    """
    sjno = input('상세 조회할 학생번호는?')

    row = SungJukDAO.selectone_sungjuk(sjno)

    print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
          f'{row[5]} {row[6]} {row[7]} {row[8]}')


# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return:
    """
    sjno = input('수정할 학생번호는?')
    # 튜플객체를 수정하기 위해 리스트 객체로 변환
    sj = list(SungJukDAO.selectone_sungjuk(sjno))

    if sj[0]:  # 만일, 수정할 데이터가 존재한다면
        sj[1] = input(f'새로운 이름은? ({sj[1]}) : ')
        sj[2] = int(input(f'새로운 국어는? ({sj[2]}) : '))
        sj[3] = int(input(f'새로운 영어는? ({sj[3]}) : '))
        sj[4] = int(input(f'새로운 수학은? ({sj[4]}) : '))
        # 조회한 결과를 클래스 타입으로 변경후 다시 성적처리
        sj = SungJuk(sj[1], sj[2], sj[3], sj[4])
        SungJukService.compute_sungjuk(sj)

        rowcnt = SungJukDAO.update_sungjuk(sj, sjno)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다!')

    else:
        print('데이터가 존재하지 않아요!!')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터 삭제
    :return:
    """
    sjno = input('삭제할 학생번호는?')
    rowcnt = SungJukDAO.delete_sungjuk(sjno)
    print(f'{rowcnt} 건의 데이터가 삭제되었습니다!')


# 성적처리 프로그램 종료
def exit_program():
    """
    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
