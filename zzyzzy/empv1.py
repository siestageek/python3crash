import sys
emps = []

def load_employees():
    print('프로그램을 초기화합니다...')
    print('프로그램이 성공적으로 초기화되었습니다.')


def show_menu():
    main_menu = '''
    --------------------
    사원관리 프로그램 v1
    --------------------
    1. 사원 정보 추가
    2. 사원 정보 조회
    3. 사원 정보 상세조회
    4. 사원 정보 수정
    5. 사원 정보 삭제
    0. 프로그램 종료
    --------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


def add_employee():
    print('사원 정보를 등록합니다...')


def read_employee():
    print('모든 사원 정보를 조회합니다...')


def readone_employee():
    print('특정 사원의 상세 정보를 조회합니다...')


def modify_employee():
    print('특정 사원의 정보를 수정합니다...')


def remove_employee():
    print('특정 사원의 정보를 제거합니다...')


def exit_program():
    print('프로그램을 종료합니다!')
    sys.exit(0)
