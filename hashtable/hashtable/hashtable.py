
from operator import indexOf


class Hashtable(object):
    def __init__(self) :
        self.size = 1024
        self.map = [None]*self.size


    def set(self , key , value ):
        idx = self.hash(key)

        if not self.map[idx]:
                self.map[idx] = [[key , value]]
        else :
            self.map[idx].append([key , value])

    def get(self , key):
        _key = self.hash(key)
        if self.map[_key]:
            for i in  self.map[_key]:
                if len(self.map[_key]) ==1:
                    return self.map[_key][0][1]
                else:
                    for j  in range(len(self.map[_key]) > 1):
                        if i[j]== key:
                            return i[1]
            return i[1]
        else:
            return None


    def delete(self , key):
        _key = self.hash(key)
        self.map[_key] = None


    def contains(self , key):
        idx = self.hash(key)
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

    

# def repeated_word(string):
#     ascii_sum = 0
#     i=0
#     lst = string.split()
#     dict = []
#     for i in lst:
#         dict.append({i: lst.index(i)})
#     for x in dict[i]['key'] :
#             ascii_sum += ord(i)
#             i += 1

    
#     return ascii_sum



if __name__ == '__main__':
    hashtable = Hashtable()
    hashtable.set("cloud", "AWS")
    hashtable.set("colud", "ayat")
    hashtable.set("clou", "ayat") 
    # print(hashtable.map[0])
    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item[0])

    # print(hashtable.contains("ayat"))
    # print(hashtable.contains("cloud"))
    # print(hashtable.contains("cloud"))
    # print(hashtable.hash("cloud"))
    # print(hashtable.hash("cloud"))
    # print(hashtable.hash("ayat"))
    # print(hashtable.get("clo"))
    # print(hashtable.hash("Django"))
    print(hashtable.get("colud"))
    # hashtable.delete("clou")
    # print(hashtable.get("clou"))

    # print(repeated_word('hi hhi hiii'))