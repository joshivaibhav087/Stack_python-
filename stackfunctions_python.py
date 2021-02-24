class Stack():
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.arr = []

    def isfull(self):
        if len(self.arr) == self.maxlength:
            return True
        return False

    def isempty(self):
        if len(self.arr) == 0:
            return True
        return False

    def push(self,item):
        if self.isfull() == True:
            print("satck is full")
        else:
            self.arr.append(item)

    def pop(self):
        if self.isempty() == True:
            print("stack is empty")
        else:
            print(self.arr.pop())
    def show_data(self):
        if self.isempty() == True:
            print("no data to show")
        else:
            for i in self.arr:
                print(i)

    def peak(self,index):
        if self.isempty() == True:
            print("no data")
        else:
            return self.arr[index]

    def top(self):
        p = len(self.arr)
        return self.arr[p-1]
    

    def sortedstack(self):
        temp = self.arr
        n = len(temp)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if temp[j] > temp[j+1]:
                    temp[j], temp[j+1] = temp[j+1], temp[j]
        return temp




        
        
        
        
        
       
            
            
     



            
