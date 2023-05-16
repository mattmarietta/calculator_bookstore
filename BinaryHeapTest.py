import BinaryHeap as Bh


def main():
    binaryheap = Bh.BinaryHeap()
    print("--------------------")
    print("add(3)")
    #print(binaryheap.add(2))
    #16, 19, 34, 2, 11, 33, 9, 6, 33
    print(binaryheap.add(16))
    print(binaryheap.add(19))
    print(binaryheap.add(34))
    print(binaryheap.add(2))
    print(binaryheap.add(11))
    print(binaryheap.add(33))
    print(binaryheap.add(9))
    print(binaryheap.add(6))
    print(binaryheap.add(33))
    print(binaryheap.size())
    print(binaryheap.bf_order())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())
    print(binaryheap.remove())



if __name__ == "__main__":
    main()

