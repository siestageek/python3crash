import sys
emps = []

def load_employees():
    print('프로그램을 초기화합니다...')
    global emps
    dicts = []

    with open('employees.csv') as f:
        datas = f.readlines()

    for data in datas:
        item = data.strip().split(',')
        d = {'empno':item[0], 'fname':item[1], 'lname':item[2],
             'email':item[3], 'hdate':item[4], 'jobid':item[5],
             'sal':item[6], 'deptid':item[7]}
        dicts.append(d)

    emps = dicts

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


def input_employee():
    emp = {}
    emp['empno'] = input('사원번호는?')
    emp['fname'] = input('이름은?')
    emp['lname'] = input('성은?')
    emp['email'] = input('이메일은?')
    emp['hdate'] = input('입사일은?')
    emp['jobid'] = input('직책은?')
    emp['sal'] = input('급여는?')
    emp['deptid'] = input('부서번호는?')
    return emp


def save_employee(emp):
    row = (f"{emp['empno']},{emp['fname']},{emp['lname']},"
           f"{emp['email']},{emp['hdate']},{emp['jobid']},"
           f"{emp['sal']},{emp['deptid']}\n")
    with open('employees.csv', 'a') as f:
        f.write(row)
    emps.append(emp)


def add_employee():
    print('사원 정보를 등록합니다...')
    emp = input_employee()
    save_employee(emp)


def read_employee():
    print('모든 사원 정보를 조회합니다...')
    result = ''
    for emp in emps:
        result += (f"{emp['empno']}\t{emp['fname']}"
                   f"\t{emp['jobid']}\t{emp['deptid']}\n")
    print(result)


def readone_employee():
    print('특정 사원의 상세 정보를 조회합니다...')


def modify_employee():
    print('특정 사원의 정보를 수정합니다...')


def remove_employee():
    print('특정 사원의 정보를 제거합니다...')


def exit_program():
    print('프로그램을 종료합니다!')
    sys.exit(0)
