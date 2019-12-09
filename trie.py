from node import Node

class Trie:
    def insert(self, node, word):
        if len(word) <= 0: 
            char = "/"
            if char not in node.childs:
                node.childs[char] = Node(char)
            return

        char = word.pop(0)

        if char not in node.childs:
            node.childs[char] = Node(char)

        self.insert(node.childs[char], word)


    def print_trie(self, root: Node):
        for v in root.childs.values():
            self.print_path(v, [])

    def print_path(self, node, path):
        if node.val == "/":
            result = "".join(path) 
            print(result)
        
        for c in node.childs.values():
            p = path[:] 
            p.append(node.val)
            self.print_path(c, p)
        

    def __init__(self, words):
        self.root = Node("⚡️")
        self.nodes = set()

        for w in words:
            w_list = list(w) 
            self.insert(self.root, w_list)

        self.print_trie(self.root)