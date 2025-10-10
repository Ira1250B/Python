class Book:
    def __init__(b,t,a,p):
        b.t=t
        b.a=a
        b.p=p
    
    def display_details(b):
        return f'Book Title: {b.t},Name of Author: {b.a},Prise of the Book: {b.p}'
class Price(Book):
    def display_details(b):
        b.p-=b.p*0.1
        return f'Updated price: {b.p}'
    #a Printing details of two different objects
book1=Book('The Fishermen','Chigozie Obioma',395)
book2=Book('The Museum of Innocence','Orhan Pamuk',599)
print(book1.display_details(),"\n")
print(book2.display_details(),"\n")
#updated price of first book
book=Price('The Museum of Innocence','chigozie',395)
print(book.display_details())