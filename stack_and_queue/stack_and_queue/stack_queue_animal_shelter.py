class Node :
    def __init__(self , type ,value , next = None):
        self.type = type
        self.value = value
        self.next = next

class StackQueueAnimalShelter:
    
    def __init__(self):
        self.front = None

    def enqueue(self , animal , value):
        if animal == 'dog' or animal =='cat':
            if self.front == None:
                self.front= Node(animal, value ,None)
                return 
            itr = self.front
            while itr.next:
                itr = itr.next
            itr.next = Node(animal , value,  None)
            return 

    def dequeue_specific_one(self , pref , value):

        if pref == 'cat' or pref == 'dog':
            if self.front == None:
                raise('empty')
            if self.front.type == pref:
                node = self.front.type
                self.front = self.front.next
                return f'{node} : {value} is dequeued'
            itr = self.front
            while itr :
                if itr.next.type == pref and itr.next.value == value:
                    node = itr.next.type
                    valuee = itr.next.value
                    itr.next = itr.next.next
                    return f'{node} : {valuee} is dequeued'
                elif itr.next.type == pref and itr.next.value != value or itr.next.type != pref and itr.next.value == value:
                    itr = itr.next
                itr = itr.next

            # return 'Null'

    def dequeue_first_one(self , pref):
        if pref == 'cat' or pref == 'dog':
            if self.front == None:
                raise('empty')
            if self.front.type == pref:
                node = self.front.type
                self.front = self.front.next
                return f'{node}  is dequeued'
            itr = self.front
            while itr :
                if itr.next.type == pref :
                    node = itr.next.type
                    valuee = itr.next.value
                    itr.next = itr.next.next
                    return f'{node}  is dequeued'
                itr = itr.next

      
    def __str__(self):
            if self.front is None:
                print('empty list')
                return

            itr= self.front
            llstr= '"'
            while itr :
                llstr= llstr + '{' + str(itr.type)+ ':' + str(itr.value) +'}'+'-> ' 
                itr=itr.next
            llstr+='NULL"'
            return llstr



if __name__ == '__main__':
    animal_shelter = StackQueueAnimalShelter()

    animal_shelter.enqueue('cat'  , 'lolo')
    animal_shelter.enqueue('dog' ,'roro')
    animal_shelter.enqueue('dog' , 'meme' )
    animal_shelter.enqueue('cat'  , 'soso')
    animal_shelter.enqueue('dog' , 'jojo' )
    animal_shelter.enqueue('anything' , 'anyname')
    print (animal_shelter.__str__())
    print(animal_shelter.dequeue_specific_one('dog' , 'jojo' ))
    print (animal_shelter.__str__())
    print(animal_shelter.dequeue_first_one('cat'))
    print (animal_shelter.__str__())
    print(animal_shelter.dequeue_first_one('dog'))
    print (animal_shelter.__str__())
    print(animal_shelter.dequeue_specific_one('cat' , 'soso' ))
    print (animal_shelter.__str__())
    print(animal_shelter.dequeue_specific_one('camel' , 'soso' ))
    