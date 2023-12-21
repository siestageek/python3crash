# 성적처리 프로그램 V2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 입력 데이터 선언
names = ['혜교', '수지', '지현']
kors = [99, 65, 87]
engs = [98, 54, 77]
mats = [99, 88, 69]
tots = []
avgs = []

# 성적처리
tots.append(kors[0] + engs[0] + mats[0])
avgs.append(tots[0] / 3)

tots.append(kors[1] + engs[1] + mats[1])
avgs.append(tots[1] / 3)

tots.append(kors[2] + engs[2] + mats[2])
avgs.append(tots[2] / 3)

# 결과출력
print(f'이름: {names[0]:s}, 국어: {kors[0]}, 영어: {engs[0]}, 수학: {mats[0]}')
print(f'총점: {tots[0]:d}, 평균: {avgs[0]:.1f}')

print(f'이름: {names[1]:s}, 국어: {kors[1]}, 영어: {engs[1]}, 수학: {mats[1]}')
print(f'총점: {tots[1]:d}, 평균: {avgs[1]:.1f}')

print(f'이름: {names[2]:s}, 국어: {kors[2]}, 영어: {engs[2]}, 수학: {mats[2]}')
print(f'총점: {tots[2]:d}, 평균: {avgs[2]:.1f}')
