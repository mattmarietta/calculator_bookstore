import Book
import ChainedHashTable
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import MaxQueue
import time
import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
                #self.bookIndices.add(key, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
            #adding book key and index to a hash table

    def addBookByPrefix(self, prefix):
        if prefix != "":
            b = self.sortedTitleIndices._return_node(prefix).v
            if b is not None:
                book = self.bookCatalog.get(b)
                if prefix <= book.title:
                    if book.title[0:len(prefix)] == prefix:
                        self.shoppingCart.add(book)
                        return book.title
        return None

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def getCartBestSeller(self):
        tiempo = time.time()
        print("getCartBestSeller returned")
        print(self.shoppingCart.max().title)
        w_time = time.time() - tiempo
        print(f"Completed in {tiempo} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u}\nCompleted in {elapsed_time} seconds")

    def addBookByKey(self, key):
        # First search hash table bookIndices for the index corresponding to the given key
        begin_time = time.time()
        index = self.bookIndices.find(key)
        if index is not None:
            book = self.bookCatalog.get(index)
            self.shoppingCart.add(book)
        elapsed_time = time.time() - begin_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        elapsed_time = time.time() - start_time
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == 2:
            algorithms._quick_sort_f(self.bookCatalog, 0, (len(self.bookCatalog)-1))
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == 3:
            algorithms._quick_sort_r(self.bookCatalog, 0, (len(self.bookCatalog)-1))
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        else:
            return False

    def display_catalog(self, n):
        for i in range(n):
            if i >= len(self.bookCatalog):
                break
        print(self.bookCatalog[i])

    def bestsellers_with(self, infix, structure, n = 0):
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")

        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                # FIXME: Insert the rest of the implementation here
                cnt = 0
                for i in range(self.bookCatalog.size()):
                    libro = self.bookCatalog.get(i)
                    if infix in libro.title:
                        if structure == 1:
                            best_sellers.add(libro.rank, libro)
                        else:
                            libro.rank = (-1 * libro.rank)
                            best_sellers.add(libro)
                        cnt += 1
                        if cnt is n:
                            break
                if structure == 1:
                    for libro in reversed(best_sellers.in_order()):
                        print(libro.v)
                        print()
                else:
                    while best_sellers.size() > 0:
                        libro = best_sellers.remove()
                        libro.rank = (-1 * libro.rank)
                        print(libro)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with(\"{infix}\", {structure}, {n}) in {elapsed_time} seconds")
