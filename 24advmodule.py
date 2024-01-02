# 사용자 모듈 불러오기
# 모듈은 사용자가 만든 파이썬 소스를 이용
# import 명령을 이용해서 불러옴

import clouds2024

# 모듈 사용하기 1 - 모듈명.함수명
print(clouds2024.add(10, 5))
print(clouds2024.mul(10, 5))

# 모듈 사용하기 2 - 모듈명 생략
# from 모듈명 import 함수명  (비추)
from clouds2024 import add
#from clouds2024 import mul
from clouds2024 import add, mul

add(10, 5)
mul(10, 5)

# 모듈 사용하기 3 - 모듈명 생략
# from 모듈명 import *  (더 비추)
from clouds2024 import *

add(10, 5)
mul(10, 5)

# 모듈 사용하기 4 - 모듈명 생략
# import 모듈명 as 별칭 (추천!)
import clouds2024 as cld

print(cld.add(10, 5))
print(cld.mul(10, 5))


# 패키지
# 서로 관련있는 모듈들을 특정 폴더에 모아둔 것
# 모듈 구성시 __init__.py 파일이 필요할 수 있음 (py3.3부터는 생략 가능)
# 세분화된 모듈명은 .으로 구분해서 작성
import zzyzzy.math as math

print(math.add(10, 5))

# 모듈의 적절한 저장 위치
# 모듈이 적절히 포함되려면
# 1) 실행파일과 같은 공간(디렉토리)에 함께 있어야 함
# 단, 같은 공간내 소스들만 해당 모듈을 사용할 수 있음!
# 즉, 프로젝트내 모듈이 존재한다면 해당 모듈은
# 실행중인 프로젝트만 사용가능 (보안 - 추천!)

# 2) 모든 프로젝트에서 모듈을 사용하려면
# 계정명/appdata/local/programs/python/lib 아래에
# 모듈을 저장해두면 됌


# 외부 모듈 사용하기
# 내장 모듈이나 사용자 정의 모듈 이외에
# 다른 조직/기관이나 개인이 만든 모듈을 사용하려면
# 먼저 모듈을 다운로드해서 설치해야만 함
# pip install 모듈명
# pip install scikit-learn, pandas
# pip install Django, fastapi
# pip install pymysql

