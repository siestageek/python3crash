# 개선된 성적 클래스 - 생성자를 통해 변수 초기화
class SungJuk2:
    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'

    # __str__ : 멤버변수들의 값을 문자열화해서
    # 객체 정보를 외부에 표현할때 사용하는 특수한 함수
    def __str__(self):
        result = f'{self.name} {self.kor} {self.eng} {self.mat}'
        return result


# 성적 객체 생성 및 초기화
sj = SungJuk2('혜교', 99, 98, 99)

print(sj.name, sj.kor, sj.eng, sj.mat)

sj = SungJuk2(input('이름은?'), int(input('국어는?')),
              int(input('영어는?')), int(input('수학은?')))

print(sj.name, sj.kor, sj.eng, sj.mat)

# SungJuk 클래스의 __str__을 호출해서 객체의 내용을 출력
print(sj)

