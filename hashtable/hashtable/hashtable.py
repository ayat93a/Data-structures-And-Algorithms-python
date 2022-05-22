from ast import Return


class Hashtable(object):
    def __init__(self) :
        self.size = 1024
        self.map = [None]*self.size

    def get(self , key):
        ascii_sum = 0
        for i in key :
            i_ascii = ord(i)
            ascii_sum += i_ascii

        hash_key = (ascii_sum * 907) % self.size
        return hash_key

    def set(self , key , value ):
        idx = self.get(key)

        if not self.map[idx]:
            self.map[idx] = [[key , value]]
        else :
            self.map[idx].append([key , value])


    def contains(self , key):
        idx = self.get(key)
        if not self.map[idx]:
            return False
        else :
            return True

    def keys(self):
        pass 

    def hash(self , key):
        






if __name__ == '__main__':
    hashtable = Hashtable()
    hashtable.set("cloud", "AWS")
    hashtable.set("cloud", "ayat")
    hashtable.set("Django", "python")
    # print(hashtable.map[0])
    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item)

    print(hashtable.contains("ayat"))
    print(hashtable.contains("cloud"))
    print(hashtable.contains("cloud"))
    print(hashtable.contains("Django"))