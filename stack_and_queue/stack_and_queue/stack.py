


from inspect import stack


class Node :

        def __init__(self , value , next = None):
            self.value = value
            self.next = next


class Stack:

        def __init__(self):
            self.top = None

        
        def push(self , value):
            
            node = Node(value)
            if self.top == None:
                self.top = Node (value , None)
                return
            node = Node(value , self.top)
            self.top = node
            return
      
        
        def pop(self):

            if self.top == None:
                raise('empty stack')
            itr = self.top
            external_storage = self.top.value
            self.top = itr.next  
            return external_storage
            
           

        def peek(self):
            if self.top == None:
                raise('empty stack')
            node = self.top.value
            return node

        def is_empty(self):
            if self.top == None:
                return True
            return False


        def __repr__(self) :
                return self.__repr__()

        def to_string(self):
                self.__str__()

        def __str__(self):
                if self.top is None:
                    print('empty list')
                    return

                itr= self.top
                llstr= '"'
                while itr :
                    llstr= llstr + '{' +str(itr.value)+ '}' +'-> ' 
                    itr=itr.next
                llstr+='NULL"'
                return llstr 



        def dequeue(self):
            """
            Extracts a value from the PseudoQueue, using a first-in first-out approach.
            """
            
            if not self.stack2.is_empty():
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())

            if not self.stack1.is_empty():
                return self.stack1.pop()
            else:
                raise(Exception("Pseudo queue is empty !"))



class Pseudo_queue:

        def __init__(self):
            self.stack1 = Stack()
            self.stack2 = Stack()

        def enqueue(self , value ):
            self.stack1.push(value)
            return self.stack1


        def dequeue(self):  
            if self.stack1.top == None and self.stack2.top == None :
                raise '2 empty stacks , nothing to return'

            if self.stack2.top == None:
                itr = self.stack1.top
                while itr:
                    if itr.next == None:
                        value = itr.value
                        self.stack2.push(value)
                    itr = itr.next
            
                return f'dequeue value --> {self.stack2.pop()} '
            


        def __str__(self):
                str_stack = ''
                itr = self.stack1.top
                while itr:
                    str_stack  += '{' + str(itr.value) +'}' + '->' 
                    itr=itr.next
                str_stack += 'None'
                return str_stack
    



if __name__ == '__main__':

        stack = Stack()
        stack1 = Pseudo_queue()
        stack2 = Pseudo_queue()
        stack1.enqueue(20)
        # print(stack1.__str__())
        stack1.enqueue(15)
        # print(stack1.__str__())
        stack1.enqueue(10)
        # stack1.enqueue(5)
        # print(stack1.__str__())
        stack1.enqueue(5)
        print(stack1.__str__())
        print(stack1.dequeue())
        # print(stack1.__str__())
        # print(stack1.__str__())
        # # stack.appened()
        # stack=Stack()
        # print(stack.pop())
        # print(stack.peek())
        # print(stack.is_empty())
        # print (stack1)
        # stack1.create_queue()
        # print(stack2)
        # stack = Stack()
        # stack.push(1)
        # stack.push(2)
        # stack.push(3)
        # stack.push(4)
        # stack.push(5)
        # print(stack.pop())
        # # # stack.push(12)
        # # print(stack)
        # # stack.pop()
        # print(stack)