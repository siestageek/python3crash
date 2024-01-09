# 성적처리 프로그램 V8
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현 
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
# 성적 데이터는 데이터베이스 테이블에 저장
# 클래스 기반으로 재작성
import zzyzzy.sjv8 as sjv8

while True:
    # 프로그램 주 실행부
    menu = sjv8.show_menu()

    if menu == '1': sjv8.addsungjuk()
    elif menu == '2': sjv8.show_sungjuk()
    elif menu == '3': sjv8.showone_sungjuk()
    elif menu == '4': sjv8.modify_sungjuk()
    elif menu == '5': sjv8.remove_sungjuk()
    elif menu == '0': sjv8.exit_program()
    else: print('메뉴를 잘못 선택하셨습니다!!')
