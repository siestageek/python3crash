# 도서명, 저자, 출판사, 출간일, 정가, 판매가, 할인율, 적립금
# bkname, author, publisher, pubdate
# retail, price, pctoff, mileage

class Book:
    def __init__(self, bkname,author,publisher,pubdate,retail,pctoff):
        self.bkno = -1
        self.bkname = bkname
        self.author = author
        self.publisher = publisher
        self.pubdate = pubdate
        self.retail = retail
        self.price = -1
        self.pctoff = pctoff
        self.mileage = -1
        self.regdate = -1

    def __str__(self):
        self.price = self.retail * (1 - (self.pctoff/100))
        self.mileage = self.retail * (self.pctoff/100)

        result = (f'{self.bkname} {self.author} {self.publisher} '
                  f'{self.pubdate} {self.retail} {self.pctoff} '
                  f'{self.price} {self.mileage}')

        return result
