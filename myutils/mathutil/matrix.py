__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
class Matrix:

    def __init__(self, elemlst):
        self.elem_lst = elemlst
    def __add__(self, b):

        if len(self.elem_lst) != len(b.elem_lst):
            print("The two matrices should have equal number of rows")
            return
        if len(self.elem_lst[0]) != len(b.elem_lst[0]):
            print("The two matrices should have equal number of columns")
            return

        metsum = self.elem_lst.copy()
        for i in range(len(metsum)):
            for j in range(len(metsum[i])):
                metsum[i][j] += b.elem_lst[i][j]

        return Matrix(metsum)

    def __sub__(self,b):
        if len(self.elem_lst) != len(b.elem_lst):
            print("The two matrices should have equal number of rows")
            return
        if len(self.elem_lst[0]) != len(b.elem_lst[0]):
            print("The two matrices should have equal number of columns")
            return

        metdiff = self.elem_lst.copy()
        for i in range(len(metdiff)):
            for j in range(len(metdiff[i])):
                metdiff[i][j] -= b.elem_lst[i][j]

        return Matrix(metdiff)

    '''
    def __mul__(self,b):
        if len(self.elem_lst[0]) != len(b.elem_lst):
            print("The matrices are not bultipliable")
            return


        prodrow = len(self.elem_lst)
        prodcol = len(b.elm_lst[0])
        metprod = [[0 for j in range(prodcol)]for i in range(prodrow)]
        for i in range(prodrow):
            for j in range(prodcol):
                metprod
        for i in range(len(metprod)):
            for j in range(len(metprod[i])):
                metprod[i][j] -= b.elem_lst[i][j]

        return Matrix(metprod)

    '''
    def print(self, separator = " "):
        printstr = ""
        for i in range(len(self.elem_lst)):
            for j in range(len(self.elem_lst[i])):
               printstr += str(self.elem_lst[i][j]) + separator
            printstr = printstr.strip(separator)
            printstr += "\n"
        print(printstr)


'''
a = Matrix([[2,3,1],[7,4,6]])
b = Matrix([[6,8,3],[5,2,4]])
c = a + b
c.print()
'''