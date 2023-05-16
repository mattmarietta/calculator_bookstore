import numpy as np
#import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import re
import operator
import BinarySearchTree


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def matched_expression(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0:
                    return False
                stack.pop()

        return len(stack) == 0

    def print_expression(self, exp):
        # Split the expression into a list of variable names and everything else
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        el = re.split('\w+', exp)
        # Build the output string by appending each element from the two lists
        for i in range(len(variables)):
            var = variables[i]
            val = self.dict.find(var)
            # If we haven't reached the end of the list of variables, append the value of the corresponding variable
            if val is not None:
                variables[i] = str(val)
        p = ""
        while len(variables) > 0 and len(el) > 0:
            p += el[0] + variables[0]
            del variables[0]
            del el[0]
        while len(el) > 0:
            p += el[0]
            del el[0]
        print(p)

#calculator = Calculator()
#calculator.print_expression("d1 * (alpha + b) + ((f/d2) + r")

    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) is False:
            raise ValueError
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree().Node()
        current = t.r
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        exp = re.findall('[-+*/()]|\w+', exp)
        for i in exp:
            print(i)
            if i == "(":
                current.insert_left(BinaryTree.BinaryTree().Node())
                current = current.left
            elif i in ["+", "-", "/", "*"]:
                current.set_val(i)
                current.set_key(i)
                current.insert_right(BinaryTree.BinaryTree().Node())
                current = current.right
            elif i.isalnum():
                current.set_val(self.dict.find(i))
                current.set_key(i)
                current = current.parent
            elif i in variables:
                current.set_key(i)
                current.set_val(self.dict.find(i))
                current = current.parent
            elif i == ")":
                current = current.parent
        return t


    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        if u.left is not None and u.right is not None:
            fn = op[u.k]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left is None and u.right is None:
            if u.v is not None:
                return u.v
            raise ValueError(f"Missing value for variable {u.k}")
        elif u.left is not None:
            return self._evaluate(u.left)
        else:
            return self._evaluate(u.right)
