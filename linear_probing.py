class HashTable:
    def __init__(self, size):
        """
        Initialize the hash table.
        :param size: The size of the hash table
        """
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """
        Calculate the hash value for a key.
        :param key: The key to hash
        :return: Hash value (index)
        """
        return key % self.size

    def insert(self, key):
        """
        Insert a key into the hash table using linear probing.
        :param key: The key to insert
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            print(f"Collision at index {index} for key {key}, probing...")
            index = (index + 1) % self.size
            if index == original_index:  # The table is full
                print("Hash table is full, cannot insert key:", key)
                return
        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")

    def search(self, key):
        """
        Search for a key in the hash table using linear probing.
        :param key: The key to search for
        :return: Index of the key if found, otherwise -1
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == original_index:  # Came back to the starting point
                break
        return -1

    def display(self):
        """
        Display the contents of the hash table.
        """
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
