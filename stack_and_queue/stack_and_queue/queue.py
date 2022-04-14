
class Node :

    def __init__(self , value , next = None):
        self.value = value
        self.next = next


class Queue:

    def __init__(self):
        self.front = None



    def enqueue(self , value):
        if self.front == None:
            self.front= Node(value , None)
            return
        itr = self.front
        while itr.next:
            itr = itr.next
        itr.next = Node(value , None)
        return


    def dequeue(self):

        if self.front == None:
            raise('empty stack')
        itr = self.front
        node = self.front.value
        self.front= itr.next  
        return node

    def peek(self):
        if self.front == None:
            raise('empty stack')
        node = self.front.value
        return node

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def __repr__(self) :
            return self.__repr__()

    def to_string(self):
            self.__str__()

    def __str__(self):
            if self.front is None:
                print('empty list')
                return

            itr= self.front
            llstr= '"'
            while itr :
                llstr= llstr + '{' +str(itr.value)+ '}' +'-> ' 
                itr=itr.next
            llstr+='NULL"'
            return llstr 

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    print(queue.dequeue())
    print(queue)
    #queue.dequeue()
    # print(queue.peek())
    # print(queue)
    # print(queue.is_empty())