import os.path
import sys
from zzyzzy.Book import Book
from zzyzzy.BookDAO import BookDAO

# 클래스의 메서드 접근제한자
# public    : 어느 클래스든지 모두 접근 가능
# protected : 상속관계에 있는 클래스만 접근 가능 (파이썬 지원 x)
# default   : 같은 패키지내 클래스들끼리 접근 가능 (파이썬 지원 x)
# private   : 메서드를 정의한 클래스만 접근 가능 (메서드에 __ 추가)


class BookService:
    # 메뉴 출력
    @staticmethod
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
    @staticmethod
    def __input_book():
        try:
            bkname = input('도서명은?')
            author = input('도서 저자는?')
            publisher = input('도서 출판사는?')
            pubdate = input('도서 출간일은?')
            retail = int(input('도서 소매가는?'))
            pctoff = int(input('도서 할인율은?'))

            bk = Book(bkname,author,publisher,pubdate,retail,pctoff)

            bk.price = bk.retail * (1 - (bk.pctoff/100))
            bk.mileage = bk.retail * (bk.pctoff/100)

            return bk
        except:
            print('BookService - input_book에서 오류발생!!')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('예외내용 :', exc_obj)
            print('예외종류 :', exc_type.__name__)
            print('예외위치 :', fname, exc_tb.tb_lineno)


    @staticmethod
    def new_book():
        """
        도서 데이터 추가 (입력-처리-저장)
        :return:
        """
        print('도서데이터 추가')
        try:
            bk = BookService.__input_book()

            rowcnt = BookDAO.insert_book(bk)
            print(f'{rowcnt} 건의 도서데이터 등록됨!!')
        except:
            print('BookService - new_book에서 오류발생!!')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('예외내용 :', exc_obj)
            print('예외종류 :', exc_type.__name__)
            print('예외위치 :', fname, exc_tb.tb_lineno)


    # 모든 도서 데이터 출력
    @staticmethod
    def read_book():
        """
        모든 도서 데이터 출력 (번호/도서명/저자/출판사/판매가)
        :return:
        """
        print('도서데이터 조회')
        result = ''

        rows = BookDAO.select_book()
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]:,}\n'

        print(result)


    # 도서 데이터 상세 조회
    @staticmethod
    def readone_book():
        """
        도서 데이터 상세 조회
        :return:
        """
        bkname = input('상세 조회할 도서명은?')

        row = BookDAO.selectone_book(bkname)
        if row:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}'
                  f'{row[5]:,} {row[6]:,} {row[7]}% {row[8]:,} {row[9]}')
        else:
            print('데이터가 없어요!')

    @staticmethod
    def __reinput_book(obk):
        bkname = input(f'도서명은? ({obk[1]}) ')
        author = input(f'도서 저자는? ({obk[2]}) ')
        publisher = input(f'도서 출판사는? ({obk[3]}) ')
        pubdate = input(f'도서 출간일은? ({obk[4]}) ')
        retail = int(input(f'도서 소매가는? ({obk[5]}) '))
        pctoff = int(input(f'도서 할인율은? ({obk[7]}) '))

        bk = Book(bkname,author,publisher,pubdate,retail,pctoff)

        bk.price = bk.retail * (1 - (bk.pctoff/100))
        bk.mileage = bk.retail * (bk.pctoff/100)
        bk.bkno = obk[0]

        return bk

    # 도서 데이터 수정
    @staticmethod
    def modify_book():
        """
        도서 데이터 수정
        :return:
        """
        bkname = input('수정할 도서이름은?')
        row = BookDAO.selectone_book(bkname)

        if row:
            bk = BookService.__reinput_book(row)
            rowcnt = BookDAO.update_book(bk)
            print(f'{rowcnt} 건의 도서데이터 수정됨!!')
        else:
            print('수정할 데이터가 없어요!!')


    # 도서 데이터 삭제
    @staticmethod
    def remove_book():
        """
        도서 데이터 삭제
        :return:
        """
        bkno = input('삭제할 도서번호는?')

        rowcnt = BookDAO.delete_book(bkno)
        print(f'{rowcnt} 건의 도서데이터 삭제됨!!')


    # 도서처리 프로그램 종료
    @staticmethod
    def exit_program():
        """
        도서처리 프로그램 종료 함수
        :param: 없음
        :return: 없음
        """
        print('프로그램 종료!')
        sys.exit(0)
