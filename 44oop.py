# 소프트웨어의 좋은 설계
# 유지보수가 용이해야 함
# 높은 응집도와 낮은 결합도를 가지도록 요소(모듈)를 적절히 배치하는 것
# - 소프트웨어 설계 품질을 판단하는 기준
# 모듈: 크기와 상관없이 클래스나 패키지,
# 라이브러리와 같이 프로그램을 구성하는 임의의 요소를 의미

# 소프트웨어 레이어링layering은 소프트웨어를 계층으로 구성하는 디자인 패턴
# 각 계층은 특정 책임을 가지며, 다른 계층과는 독립적으로 개발 및 유지 관리할 수 있음

# 구조의 명확성: 소프트웨어의 구조와 각 계층의 책임을 명확하게 정의함으로써,
# 소프트웨어의 이해와 유지 관리 용이
# 확장성: 새로운 기능 추가시, 기존 레이어를 변경하지 않고, 새로운 레이어 추가
# 유지 보수성: 각 계층은 독립적으로 개발 및 유지 관리할 수 있으므로,
# 소프트웨어의 유지 보수 용이

# 3-tier 아키텍처
# 응용프로그램을 3개의 논리적 및 물리적 컴퓨팅 계층으로 구성하는 소프트웨어 아키텍처
# '프리젠테이션 계층', 데이터를 처리하는 '애플리케이션 계층',
# 그리고 애플리케이션과 연관된 데이터를 저장 및 관리하는 '데이터 계층'으로 구성
# 보다 신속한 개발, 확장성 개선, 안정성 향상, 보안성 강화

# import zzyzzy.SungJuk
from zzyzzy.SungJuk import SungJuk

# 성적을 다루는 클래스 정의
# class SungJuk:
#     def __init__(self, name, kor, eng, mat):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.mat = mat
#         self.tot = 0
#         self.avg = 0.0
#         self.grd = '가'
#
#     def __str__(self):
#         result = f'{self.name} {self.kor} {self.eng} {self.mat}'
#         return result

# 성적처리에 필요한 기능으로 구성된 클래스 정의
class SungJukService:
    # 데코레이터 (@) : 함수에 추가기능을 구현할때 사용
    @staticmethod  # 정적 메서드: 객체 선언없이 바로 사용할 수 있는 메서드
                   # 호출방법: 클래스명.함수명
                   # 정적 메서드로 정의된 함수에는 self 지정 x
    def read_sungjuk():
        name = input('이름은 ?')
        kor = int(input('국어는 ?'))
        eng = int(input('영어는 ?'))
        mat = int(input('수학은 ?'))

        # return name,kor,eng,mat
        # return [name,kor,eng,mat]
        # return ['name':name,'kor':kor,'eng':eng,'mat':mat]
        return SungJuk(name, kor, eng, mat)

    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd = '우'
        elif (sj.avg >= 70): sj.grd = '미'
        elif (sj.avg >= 60): sj.grd = '양'


# 성적서비스 호출 1
sjsrv = SungJukService()  # 서비스 클래스에 대한 객체 생성
sj = sjsrv.read_sungjuk()
sjsrv.compute_sungjuk(sj)
print(sj)

# 성적서비스 호출 2
sj2 = SungJukService.read_sungjuk()
SungJukService.compute_sungjuk(sj2)
print(sj2)

