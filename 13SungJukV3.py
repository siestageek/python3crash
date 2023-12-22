# 성적처리 프로그램 V3
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현 
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
import sys

# 입력 데이터 선언
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 프로그램 메뉴출력을 위한 변수 선언
main_menu = '''
--------------------
성적처리 프로그램 v3
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''

for i in range(100):
    # 프로그램 주 실행부
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if   menu == '1':
        print('성적데이터 추가')
        sjpos = len(avgs)   # 현재 입력된 데이터 수
        names.append(input('이름은 ? :'))
        kors.append(int(input('국어는?')))
        engs.append(int(input('영어는?')))
        mats.append(int(input('수학은?')))

        tots.append(kors[sjpos] + engs[sjpos] + mats[sjpos])
        avgs.append(tots[sjpos] / 3)
        avg = avgs[sjpos]
        grd = '수' if avg >= 90 else \
        '우' if avg >= 80 else \
        '미' if avg >= 70 else \
        '양' if avg >= 60 else '가'
        grds.append(grd)

    elif  menu == '2':
        print('성적데이터 조회')
        for i in range(len(names)):
            print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {mats[i]}')

    elif  menu == '3':
        print('성적데이터 상세조회')

    elif  menu == '4':
        print('성적데이터 수정')
    elif  menu == '5':
        print('성적데이터 삭제')
    elif  menu == '0':
        print('프로그램 종료!')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')

