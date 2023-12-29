# 한글이 포함된 문자열에 간격 맞추기 솔루션을 제공하는 라이브러리
import unicodedata

def preFormat(string, width, align='<', fill=' '):
    count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in string))
    return {
        '>': lambda s: fill * count + s,
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2) + s + fill * (count / 2 + count % 2)
    }[align](string)
