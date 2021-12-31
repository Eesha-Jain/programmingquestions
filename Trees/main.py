class Node:
    def __init__(self, value, nodeList):
        self.value = value
        self.nodesList = nodeList

def traverse(currentNode):
    print("Current Node: " + str(currentNode.value))
    length = len(currentNode.nodesList) 

    if (length == 0):
        print("No attached nodes")
        return

    num = int(input("Input a number from 1 - " + str(length) + ": "))

    if (num > 0 and num <= length):
        traverse(currentNode.nodesList[num - 1])
    else:
        traverse(currentNode.nodesList[0])

node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [node1, node2, node3])
node5 = Node(5, [node1, node2])
node6 = Node(6, [node4, node5])
node7 = Node(7, [])
node8 = Node(8, [node7])
node9 = Node(9, [node7, node8])
node10 = Node(10, [node6, node9])

traverse(node10)