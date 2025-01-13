class HashTable:
    def __init__(self, size):
        
        self.size = size
        self.table = [None] * size

    def primary_hash(self, key):
       
        return key % self.size

    def secondary_hash(self, key):
        
        return 1 + (key % (self.size - 1))

    def insert(self, key):
       
        index = self.primary_hash(key)
        step = self.secondary_hash(key)
        original_index = index
        i = 0  # Number of attempts

        while self.table[index] is not None:
            print(f"Collision at index {index} for key {key}, resolving using double hashing...")
            i += 1
            index = (original_index + i * step) % self.size
            if i >= self.size:  # The table is full
                print("Hash table is full, cannot insert key:", key)
                return

        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")

    def search(self, key):
        
        index = self.primary_hash(key)
        step = self.secondary_hash(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            i += 1
            index = (original_index + i * step) % self.size
            if i >= self.size:  # All slots checked
                break
        return -1

    def display(self):
      
        print("Hash Table:")
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value}")


# Example usage
hash_table = HashTable(size=7)

keys_to_insert = [10, 20, 5, 7, 15, 25, 35]

print("\nInserting keys:")
for key in keys_to_insert:
    hash_table.insert(key)

hash_table.display()

print("\nSearching keys:")
keys_to_search = [15, 25, 30]
for key in keys_to_search:
    index = hash_table.search(key)
    if index != -1:
        print(f"Key {key} found at index {index}.")
    else:
        print(f"Key {key} not found.")
