# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.childs = dict()
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if self.childs.get(char) is not None:
            self.childs[char] = TrieNode()
            self.childs[char].is_word = True

    def suffixes(self, suffix = ''):
        ## Function that collects the suffix for 
        ## all complete words below this point
        
        suffix_to_check = suffix
        node = self
        while suffix_to_check != '':
            char = suffix_to_check[0]
            node = node.childs.get(char)
            if node == None:
                return []

            suffix_to_check = suffix_to_check[1:]

        suffixes_list = node.suffixes_rec('')

        return suffixes_list
    
    def suffixes_rec(self, suffix):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        suffixes_list = []
        if self.is_word and suffix != '':
            suffixes_list.append(suffix)
        
        for child in self.childs.keys():
            suffixes_list += self.childs.get(child).suffixes_rec(suffix + child)

        return suffixes_list

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if current_node.childs.get(char) is None:
                current_node.childs[char] = TrieNode()

            current_node = current_node.childs.get(char)

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if current_node.childs.get(char) is None:
                return None #trie with prefix not existing!

            current_node = current_node.childs.get(char)

        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
# interact(f,prefix='');

def test_function(input, expected_result):
    if MyTrie.root.suffixes(input) == expected_result:
        print('Pass')
    else:
        print('Fail')

test_function('', ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod'])
test_function('a', ['nt', 'nthology', 'ntagonist', 'ntonym'])
test_function('ant', ['hology', 'agonist', 'onym'])
test_function('anth', ['ology'])
test_function('anthology', [])
test_function('c', [])
test_function('fu', ['n', 'nction'])
