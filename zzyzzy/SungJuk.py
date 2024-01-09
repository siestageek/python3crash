class SungJuk:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'

    def __str__(self):
        result = f'{self.name} {self.kor} {self.eng} {self.mat}\n' \
                 f'{self.tot} {self.avg} {self.grd} '
        return result
