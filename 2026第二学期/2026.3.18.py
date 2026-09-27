class Book():
    def __init__(self,title:str,author:str,pages:int):
        self.title: str = title
        self.author:str = author
        self.pages:int = pages
    def display(self):
        print('='*50)
        print(f'书名:{self.title}')
        print(f'作者:{self.author}')
        print(f'页数:{self.pages:.2f}')
if __name__ == '__main__':
    title = input('请输入书名:')
    author = input('请输入作者:')
    pages = int(input('请输入页数:'))
    book = Book(title,author,pages)
    book.display()