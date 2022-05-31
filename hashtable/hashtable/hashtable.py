
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

    # def keys(self):
    #     lst = []
    #     for item in self.map:
    #         if item:
    #             for i in item :
    #                 for x in i.keys():
    #                     lst.append(x)
    #     return lst

    def hash(self , key):
        ascii_sum = 0
        for i in key :
            i_ascii = ord(i)
            ascii_sum += i_ascii

        hash_key = (ascii_sum * 907) % self.size
        return hash_key

    

def repeated_word(string):
    ascii_sum = 0
    i=0
    lst = string.split()
    dict = []
    for i in lst:
        dict.append({i: lst.index(i)})
    for x in dict[i]['key'] :
            ascii_sum += ord(i)
            i += 1

    
    return ascii_sum

def leftJoin(hash1, hash2):

    hash3 = Hashtable()

    for key in hash1.keys():        
        if hash2.contains(key):
            hash3.set(key, [hash1.get(key), hash2.get(key)])
        else:
            hash3.set(key, [hash1.get(key), 'Null'])
        
    return hash3

if __name__ == '__main__':
    hashtable = Hashtable()
    hashtable.set("cloud", "AWS")
    hashtable.set("cloud", "ayat")
    # print(hashtable.map[0])
    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item[0])

    print(hashtable.contains("ayat"))
    print(hashtable.contains("cloud"))
    print(hashtable.contains("cloud"))
    print(hashtable.hash("cloud"))
    print(hashtable.hash("cloud"))
    print(hashtable.hash("ayat"))
    # print(repeated_word('hi hhi hiii'))