class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children[ch] = node
            current = node
        current.endOfString = True

    def searchString(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        return current.endOfString

    def startsWith(self, prefix):
        current = self.root
        for ch in prefix:
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        return True

    def deleteString(self, word):
        def _delete(root, word, index):
            ch = word[index]
            currentNode = root.children.get(ch)
            if currentNode is None:
                return False
            if len(currentNode.children) > 1:
                _delete(currentNode, word, index+1)
                return False
            if index == len(word) - 1:
                if len(currentNode.children) >= 1:
                    currentNode.endOfString = False
                    return False
                else:
                    root.children.pop(ch)
                    return True
            if currentNode.endOfString:
                _delete(currentNode, word, index+1)
                return False
            canDelete = _delete(currentNode, word, index+1)
            if canDelete:
                root.children.pop(ch)
                return True
            return False

        if self.searchString(word):
            _delete(self.root, word, 0)
# Create trie object
trie = Trie()

# Insert words
trie.insertString("car")
trie.insertString("care")
trie.insertString("cat")
trie.insertString("dog")

# Search full words
print(trie.searchString("car"))    # True
print(trie.searchString("care"))   # True
print(trie.searchString("cat"))    # True
print(trie.searchString("dog"))    # True
print(trie.searchString("ca"))     # False (only prefix)
print(trie.searchString("can"))    # False (not inserted)

# Check prefixes
print(trie.startsWith("ca"))       # True (car, care, cat)
print(trie.startsWith("car"))      # True (car, care)
print(trie.startsWith("do"))       # True (dog)
print(trie.startsWith("z"))        # False

# Delete words
trie.deleteString("care")
print(trie.searchString("care"))   # False
print(trie.searchString("car"))    # True (still exists)

trie.deleteString("car")
print(trie.searchString("car"))    # False
print(trie.searchString("cat"))    # True

trie.deleteString("cat")
print(trie.searchString("cat"))    # False

trie.deleteString("dog")
print(trie.searchString("dog"))    # False
