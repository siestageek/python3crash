import sys
from zzyzzy.Book import Book
from zzyzzy.BookDAO import BookDAO


# 메뉴 출력
def show_menu():
    """
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
--------------------
도서관리 프로그램 v1
--------------------
1. 도서 데이터 추가
2. 도서 데이터 조회
3. 도서 데이터 상세조회
4. 도서 데이터 수정
5. 도서 데이터 삭제
0. 프로그램 종료
--------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 도서 데이터 추가 (입력-처리-저장)
def new_book():
    """
    도서 데이터 추가 (입력-처리-저장)
    :return: 
    """
    print('도서데이터 추가')

    pass


# 모든 도서 데이터 출력
def read_book():
    """
    모든 도서 데이터 출력 (번호/도서명/저자//출판사/판매가)
    :return:
    """
    print('도서데이터 조회')
    pass


# 도서 데이터 상세 조회
def readone_book():
    """
    도서 데이터 상세 조회
    :return: 
    """
    bkname = input('상세 조회할 도서명은?')
    pass


# 도서 데이터 수정
def modify_book():
    """
    도서 데이터 수정
    :return:
    """
    bkno = input('수정할 도서번호는?')
    pass


# 도서 데이터 삭제
def remove_book():
    """
    도서 데이터 삭제
    :return:
    """
    bkno = input('삭제할 도서번호는?')
    pass


# 도서처리 프로그램 종료
def exit_program():
    """
    도서처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
