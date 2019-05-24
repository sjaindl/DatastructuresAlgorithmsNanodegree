import sys
from queue import PriorityQueue

class CharTuple:
    def __init__(self, frequency, char):
        self.frequency = frequency
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

class HuffmanCoding:
    def __init__(self, frequency, char, left = None, right = None):
        self.frequency = frequency
        self.char = char

        self.left = left
        self.right = right

    def __lt__(self, tuple2):
        return tuple2.frequency > self.frequency
    
    def __gt__(self, tuple2):
        return tuple2.frequency < self.frequency

    def __le__(self, tuple2):
        return tuple2.frequency >= self.frequency

    def __ge__(self, tuple2):
        return tuple2.frequency <= self.frequency

def huffman_encoding(data):
    # 0. validity checks
    if data == None or data == '':
        return data, None

    # 1. determine frequencies of each character
    frequency_map = dict()
    for char in data:
        if frequency_map.get(char) != None:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    
    # 2. sort chars by frequency. This is a task typically accomplished by a priority queue.
    pq = PriorityQueue()
    for key in frequency_map:
        tuple = CharTuple(frequency_map[key], key)
        pq.put(tuple)

    # 3. build tree until only 1 element is left in priority queue:
    while pq.qsize() > 1:
        element_one = pq.get()
        element_two = pq.get()
        
        sum = element_one.frequency + element_two.frequency
        tuple = CharTuple(sum, '*')

        tuple.left = element_one
        tuple.right = element_two

        pq.put(tuple) 

    # 4. get head of Hufmann tree (this is the remaining element in the pq):
    tree_head = pq.get()

    print(tree_head)

    # 5. build codes
    codes = codes_rec(tree_head, '', {})

    # 6. encode data
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    #encoded_data = encode_rec(tree_head, '')

    return encoded_data, tree_head

def codes_rec(node, prefix, codes):
    
    if not node.left and not node.right:
        codes[node.char] = prefix

    if node.left:
        codes_rec(node.left, prefix + '0', codes)
    if node.right:
        codes_rec(node.right, prefix + '1', codes)

    return codes

def huffman_decoding(data,tree):
    decoded_data = ''
    node = tree
    for code in data:
        if code == '0':
            node = node.left
        elif code == '1':
            node = node.right

        if node.left == None and node.right == None: 
            # leave reached - decode char and reset node to tree
            decoded_data += node.char
            node = tree

    return decoded_data

if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



print('*** Test HuffmanCoding ***')

sentence = ''
encoded_data, tree = huffman_encoding(sentence)
print ("The content of the encoded data is: {}\n".format(encoded_data))
assert encoded_data == '' and tree == None, "Encoded data should be empty and tree None"

sentence = None
encoded_data, tree = huffman_encoding(sentence)
assert encoded_data == None and tree == None, "Encoded data and tree should be None"

sentence = 'Udacity'
encoded_data, tree = huffman_encoding(sentence)
encoded_size = sys.getsizeof(int(encoded_data, base=2))
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
assert encoded_data > '', "Encoded data is empty!"
decoded_data = huffman_decoding(encoded_data, tree)
decoded_size = sys.getsizeof(decoded_data)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
assert encoded_size < decoded_size, "Encoded string not smaller than original string!"
assert decoded_data == sentence, "String war not correctly decoded!"

print('*** Success ***')
