class Hashtable:
    def __init__(self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i , value in enumerate(self.data_map):
            print(i,":",value)


my_hash_table=Hashtable()

my_hash_table.print_table()