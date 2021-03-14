'''
5
79
355
iexwncc
30
ginmrgx
79
166
zklmwzj
36
hgyryzw
63
198
qatidxf
58
tanxbuc
84
619
ppkyqxs
52
gbpxxej
30
331
zhkbycr
21
ciftybq
79
'''
class Book:
    def __init__(self,pages,title,price,id,author):
        self.pages=pages
        self.title=title
        self.price=price
        self.id=id
        self.author=author
class BookStore:
    def __init__(self,bookList):
        self.bookList=bookList
    def searchBookbyPages(self,pages):
        for book in self.bookList:
            if(book.pages==pages):
                return book
        return None
    def countBookbyAuthor(self):
        auth={}
        for book in self.bookList:
            if(book.author not in auth):
                auth[book.title]=1
            else:
                auth[book.title]+=1
        return auth
T=int(input())
books=[]
for test in range(T):
    id=int(input())
    price=int(input())
    title=input()
    pages=int(input())
    author=input()
    books.append(Book(id,title,price,pages,author))
bookTofind=int(input())
bStore=BookStore(books)
bookobj=bStore.searchBookbyPages(bookTofind)
print(bookobj.pages)
print(bookobj.id)
print(bookobj.price)
print(bookobj.title)
bCount=bStore.countBookbyAuthor()
for b in bCount.keys():
    print(b,bCount[b])


