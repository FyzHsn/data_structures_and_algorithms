class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True

        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
                    

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None          

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False 
        for idx in range(0, len(self.map[key_hash])):
            if self.map[key_hash][idx][0] == key:
                self.map[key_hash].pop(idx)
                return True
        

    def __repr__(self):
        items = []
        for item in self.map:
            if item is not None:
                items.append(str(item)) 
        return (", ".join(items))      

if __name__ == "__main__":
    h = HashMap()
    h.add('Bob', '123456')
    h.add('Rob', '767657')
    h.add('Cob', '980980')
    h.add('Job', '098098')
    
    print(h)
    h.delete('Bob')
    h.add('Cob', '111111')
    print(h)
