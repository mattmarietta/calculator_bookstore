import Calculator
import BookStore
import DLList


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "2":
            again = 'Y'
            while again.lower() == 'y':
                var = input("Enter a variable: ")
                val = float(input("Enter its value: "))
                calculator.set_variable(var, val)
                again = input("Enter another variable? Y/N ")
        elif option == "3":
            exp = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(exp):
                calculator.print_expression(exp)
            else:
                print("Invalid expression")
        elif option == "4":
            expression = input("Enter the expression: ")
            result = calculator.evaluate(expression)
            print("Evaluating expression:", end=' ')
            calculator.print_expression(expression)
            print("Result:", result)
        if ValueError:
            print("Result: Error - Not all variable values are defined.")


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            i = input("Enter book key: ")
            bookStore.addsBookByKey(i)
        elif option == "8":
            prefix = input("Introduce the prefix: ")
            added = bookStore.addBookByPrefix(prefix)
            if added is not None:
                print("Added first matched title:", added)
            else:
                print("Error: Prefix was not found.")
        elif option == "9":
            infix = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            max_titles = input("Enter max number of titles: ")
            bookStore.bestsellers_with(infix, structure, max_titles)
        elif option == "10":
            print("Choose an algorithm: ")
            print("1. - Merge Sort")
            print("2. - Quick Sort ()") #{bookStore.sort_catalog(s)}
            print("3. - Quick Sort ()") #{bookStore.sort_catalog(s_1)}
            alg_num = int(input(("Your selection: ", 1, 3)))
            if alg_num == "1":
                bookStore.sort_catalog(1)
            elif alg_num == "2":
                bookStore.sort_catalog(2)
            elif alg_num == "3":
                bookStore.sort_catalog(3)
            else:
                print("Invalid algorithm")
            if alg_num is not 1 or 2 or 3:
                return True
            else:
                print("Invalid algorithm")
        elif option == "11":
            numofbooks = int(input("Enter the number of books to display: "))
            if bookStore.bookCatalog:
                return bookStore.display_catalog(numofbooks)

        ''' 
        Add the menu options when needed
        '''

def menu_palindrome_test():
    user_input = input("Enter a word/phrase: ")
    w = DLList.DLList()
    for i in user_input.lower():
        if i.isalpha():
            w.append(i)
    if w.isPalindrome():
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")

# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_palindrome_test()


if __name__ == "__main__":
    main()
