# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        
        self.root_handler = root_handler
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler, node = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        if node == None:
            node = self.root
            
        if len(path) == 0: #we are at the leave node, set the handler here
            node.insert(handler)
            return

        if node.childs.get(path[0]) == None:
            node.childs[path[0]] = RouteTrieNode()

        self.insert(path[1:], handler, node.childs[path[0]])

    def find(self, path, node = None):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if len(path) == 1 and path[0] == '':
            return self.root_handler

        if node == None:
            node = self.root

        if len(path) == 0: #we are at the searched node, return it
            return node.handler

        if node.childs.get(path[0]) == None:
            return None
        
        return self.find(path[1:], node.childs[path[0]])

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.childs = dict()

    def insert(self, handler):
        # Insert the node as before
        self.handler = handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        self.root = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        sub_paths = self.split_path(path)
        self.root.insert(sub_paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        sub_paths = self.split_path(path)
        handler = self.root.find(sub_paths)
        if handler == None:
            handler = self.not_found_handler
        
        return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here

        if path == None or len(path) == 0:
            return []

        if path[len(path) - 1] == '/':
            path = path[0:-1] #support trailing slashes

        sub_paths = path.split('/')

        return sub_paths

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' -> test trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler'
