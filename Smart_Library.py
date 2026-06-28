import time, os
def clear():os.system("cls" if os.name=="nt" else "clear")

class Book:
    def __init__(self,title,author,year,status):
        self.title,self.author,self.year,self.status=title,author,int(year),status

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Available: {self.status}")
        print("-"*10)

checked_books=[]
found_books=[]
borrowed_books=[]
added_books=[]
books=[
    Book("monday happy","Tom",2011,True),
    Book("pena grok","Sam",2020,True),
    Book("sickness man","Jack",2025,True),
    Book("smart boy","Mohammed",2011,True),
    Book("school event","Hamada",2016,True),
]

def show_all_books():
    for book in books:
        book.display_book()


def add_new_book():
    while True:
            new_title=input("enter the name of a new book: ".title())
            new_author=input("enter the name of an author: ".title())

            while True:
                new_year=input("enter the year of book: ".title())
                if new_year.isdigit():
                    break  
            
            books.append(Book(new_title,new_author,new_year,True))
            added_books.append(Book(new_title,new_author,new_year,True))

            print("book added successfully ".title())
            time.sleep(1)

            if input("Add another book? [Y/n]: ").lower()!="y":
                break


def show_added_books():
    for book_added in added_books:
        book_added.display_book()


def borrow_a_book():
    while True:
        print("Borrow By: \n")
        print("1. Title")
        print("2. Author")
        print("3. Year")
        print("4. Status\n")
        
        borrow_choice=input("enter your choice: ".title())
        print("you can only these books \n","*"*10)
        for book in books:
            if book.status==True:
                book.display_book()
        if borrow_choice=="1":
            title=input("enter the title of book: ".title()).strip()
            for book in books:
                if book.title.lower()==title.lower():
                    borrowed_books.append(book)
                    book.status=False
            print("Success")
            time.sleep(1)

        elif borrow_choice=="2":
            author=input("enter the author: ".title()).strip()
            for book in books:
                if book.author.lower()==author.lower():
                    borrowed_books.append(book)
                    book.status=False
            print("Success")
            time.sleep(1)



        elif borrow_choice=="3":
                while True:
                    year=input("enter the year: ".title()).strip()
                    if year.isdigit():
                        break
                    else:
                        print("please, enter a valid year".title())

                for book in books:
                    if ((book.year))==int(year):
                        borrowed_books.append(book)
                        book.status=False
                        print(f"{book.title} borrowed ")
                    
                        time.sleep(1)         
                            


                    
        elif borrow_choice=="4":
            status=input("enter the status: ".title())
            for book in books:
                if book.status==True:
                    for book in books:
                        if str(book.status)==status:
                            borrowed_books.append(book)
                            book.status=False
                            print(f"book {book.title} borrowed ")
                            time.sleep(1)
                

        if len(borrowed_books)==0:
            print("You didnot borrow any books".title())


        if input("Another?: ").lower()!='y':
            break

def show_borrowed_books():
    for book in borrowed_books:
        book.display_book()



def check_in_book():
    for book in books:
        if book.status==False:
            print("you can only check in these books\n","*"*10)
            book.display_book()
    name_to_back=input("enter the name of book to return: ".title()).lower()
    for book in books:
        if book.title.lower()==name_to_back:

            if book.status==True:
                print("this book is already available ".title())
            elif book.status==False:
                print("book checked successfully".title())
                book.status=True
                checked_books.append(book)
                
            else:
                print("this book isnot ours ".title())
            time.sleep(1)
            break

    if input("Another: ").lower()=="y":
        check_in_book()

def show_checked_book():
    for book in checked_books:
        book.display_book()

def search_a_book():

    while True:
        print("Search By: \n")
        print("1. Title")
        print("2. Author")
        print("3. Year")
        print("4. Status\n")

        choice=input("enter your choice: ".title()).lower()

        if choice=="1":
            name_to_search=input("enter the name to search: ".title()).strip().split(" ")
            for book in books:
                for word in name_to_search:
                        word_in_title=book.title.split(" ")
                        if word.lower() in str(word_in_title).lower() or  book.title.lower()==" ".join(name_to_search).lower():
                            found_books.append(book)
                            print("success")
                            time.sleep(1)
                            break


        
        elif choice=="2":
            author_to_search=input("enter the name of author to search: ".title()).strip()
            for book in books:
                if book.author.lower()==author_to_search.lower():
                    found_books.append(book)
                    print("success")
                    time.sleep(1)
                    break


        elif choice=="3":
            year_to_search=int(input("enter the year: ".title()))
            for book in books:
                if book.year==year_to_search:
                    found_books.append(book)
                    print("success")
                    time.sleep(1)
                    break

        elif choice=="4":
            status_to_search=input("enter the status: ".title()).strip()
            for book in books:
                if str(book.status)==status_to_search.capitalize():
                    found_books.append(book)
                    print("success")
                    time.sleep(1)
                    break


        if len(found_books)==0:
            print("soory, this book not found ")
        

        if input("Another?:  ").lower()!="y":
            break



def show_found_book():
    for book in set(found_books):
        book.display_book()

def delay():
        print("*"*10)
        time.sleep(1)


while True:
    clear()
    print("welcome to our smart library\n".upper())
    
    print("CHOOSE AN ACTION: \n")
    print("1. show all books in library".title())
    print("2. add new book".title())
    print("3. borrow a book".title())
    print("4. check in a book".title())
    print("5. search a book".title())
    print("6. library statistics".title())
    print("7. Exit\n")

    
    choice=input("enter your chocie: ".title())

    clear()

    if choice=="1":
        print("displaying all books".title())
        time.sleep(1)
        print("*"*10)
        show_all_books()
        input("\ncontinue: ")

    elif choice=="2":
        add_new_book()

    elif choice=="3":
        borrow_a_book()

    elif choice=="4":
        check_in_book()

    elif choice=="5":
       search_a_book()

    elif choice=="6":
        print("\n1. show added books".title())
        print("2. show borrowed books".title())
        print("3. show checked in books".title())
        print("4. show found books".title())

        show_choice=input("enter your choice: ".title())

        if show_choice=="1":
            print("displaying added books".title())
            delay()
            if len(added_books)==0:
                print("no added books".title())
                time.sleep(1)
            
            else:
                show_added_books()

                input("\ncontinue: ")

        elif show_choice=="2":
            print("displaying borrowed books".title())
            delay()
            if len(borrowed_books)==0:
                print("no borrowed books".title())
                time.sleep(1)
            
            else:
                show_borrowed_books()

                input("\ncontinue: ")

        elif show_choice=="3":
            print("displaying checked in  books".title())
            delay()
            if len(checked_books)==0:
                print("no checked in books".title())
                time.sleep(1)
            
            else:
                show_checked_book()

                input("\ncontinue: ")
        
        elif show_choice=="4":
            print("displaying found books".title())
            delay()
            if len(found_books)==0:
                print("no found books".title())
                time.sleep(1)
            
            else:
                show_found_book()

                input("\ncontinue: ")

    elif choice=="7":
        print("Exiting ...")
        time.sleep(1)
        break

    else:
        print("invalid chocie")
        time.sleep(.66)
       



        
