# OOP : object oriented programming
# 프로그램을 명령어들의 단순 묶음이라고 보는 시각에서
# 벗어나 독립된 객체들의 모음이라고 보는 시각에 근거해서
# 프로그래밍하는 패러다임

# 프로그램을 보다 유연하게 작성할 수 있고
# 프로그램 코드의 재사용을 높일수 있으며
# 대규모 소프트웨어 개발시 유지보수가 용이해짐

# 프로그램의 각 구성요소를 실제세계의 객체와 유사하게
# 디자인해서 클래스로 정의하는 것에 중점을 둠

# ex) 성적처리 프로그램
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 출력

# 성적 입력
name = input('이름은 ?')
kor = int(input('국어는 ?'))
eng = int(input('영어는 ?'))
mat = int(input('수학은 ?'))

# 성적 처리
tot = kor + eng + mat
avg = tot / 3
grd = '가'
if (avg >= 90): grd = '수'
elif (avg >= 80): grd = '우'
elif (avg >= 70): grd = '미'
elif (avg >= 60): grd = '양'

# 결과 출력
print(f'입력: {name}, {kor}, {eng}, {mat}')
print(f'결과: {tot}, {avg:.1f}, {grd}')

# ex) 성적처리 프로그램 II
# 함수 기반 프로그래밍 : 처리코드들을 기능별로 하나의 이름으로 묶음
def readSungJuk():
    name = input('이름은 ?')
    kor = int(input('국어는 ?'))
    eng = int(input('영어는 ?'))
    mat = int(input('수학은 ?'))
    return name,kor,eng,mat

def computeSungJuk(kor,eng,mat):
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if (avg >= 90):           grd = '수'
    elif (avg >= 80):         grd = '우'
    elif (avg >= 70):         grd = '미'
    elif (avg >= 60):         grd = '양'
    return tot,avg,grd

def printSungJuk(name,kor,eng,mat,tot,avg,grd):
    print(f'입력: {name}, {kor}, {eng}, {mat}')
    print(f'결과: {tot}, {avg:.1f}, {grd}')

# 프로그램 실행
name,kor,eng,mat = readSungJuk()
tot,avg,grd = computeSungJuk(kor,eng,mat)
printSungJuk(name,kor,eng,mat,tot,avg,grd)

# ex) 성적처리 프로그램 III
# 객체지향 프로그램 : 기능을 구현하는데 사용한 함수들과 관련된 변수들을 하나로 묶음
# 성적 데이터를 담고있는 클래스와
# 성적처리에 필요한 기능들로만 구성된 클래스로 나눠 작성

# 클래스이름은 camel표기법으로 지음
# class 클래스명(상속여부):
#   생성자
#   setter/getter
#   메서드

# OOP에서의 클래스 특성
# 1. 값만 저장하는 클래스 : VO, DTO
# 2. 기능만 저장하는 클래스 : DAO, BO
# 데이터베이스 연동 클래스 : CRUD 기능 지원
# 3. UI처리만 저장하는 클래스 : UO

# 1. 값만 저장하는 클래스 : VO
# 생성자 : __init__ (매직함수)
# private 멤버변수 선언
# setter/getter : @setter, @property (@ : 데코레이터)

class SungJuk:
    # 생성자 : 클래스 객체 생성시 초기화작업을 수행하는 함수 (__init__)
    # 생성자를 통해 멤버변수 선언 및 기본값을 지정할 수 있음
    # 변수선언 : self.변수명 (public), self.__변수명 (private)
    def __init__(self):
        self.name = ''
        self.kor = 0
        self.eng = 0
        self.mat = 0
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'


# 성적 객체 생성
# 클래스에 대한 객체 생성
# (객체)변수명 = 클래스명()
sj = SungJuk()

# 객체의 멤버변수 접근 : 객체명.멤버변수명
sj.name = input('이름은?')
sj.kor = int(input('국어는?'))
sj.eng = int(input('영어는 ?'))
sj.mat = int(input('수학은 ?'))

print(sj.name, sj.kor, sj.eng, sj.mat)


