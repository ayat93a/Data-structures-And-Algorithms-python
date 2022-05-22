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
        idx = self.get(self.key)
        for item in self.map:
            if item is not None:
                return self.map[idx][self.key]

    def hash(self , key):
        ascii_sum = 0
        for i in key :
            i_ascii = ord(i)
            ascii_sum += i_ascii

        hash_key = (ascii_sum * 907) % self.size
        return hash_key

    





if __name__ == '__main__':
    hashtable = Hashtable()
    hashtable.set("cloud", "AWS")
    hashtable.set("cloud", "ayat")
    # print(hashtable.map[0])
    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item[0])

    # print(hashtable.contains("ayat"))
    # print(hashtable.contains("cloud"))
    # print(hashtable.contains("cloud"))
    # print(hashtable.keys)
    # print(hashtable.hash("cloud"))
    # print(hashtable.hash("cloud"))
    # print(hashtable.keys)
    print(hashtable.hash("ayat"))