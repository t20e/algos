def findClosestValueInBst(tree, target):
    node = tree
    closest = float('inf')
    while node is not None:
        closest = node.value if abs(node.value-target) < abd(closest-target) else closest
        if node.value < target:
            node = node.right
            continue
        node = node.left
    return closest






    # currNode = tree['nodes'][0]
    # for i in range(len(tree['nodes'])):
    #     if currNode['value'] == target:
    #         return currNode['value']
    #     elif target > currNode['value']:
    #         # check to see if were going to go to the right of node
    #         currNode = tree['nodes'][(currNode['right'])]
    #         print(currNode)
    #     elif target < currNode['value']:
    #         # check to see if were going to go to the left of node
    #         pass
    # return currNode


data = {
    "tree": {
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "13", "left": None, "right": "14", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1}
        ],
        "root": "10"
    },
    "target": 12
}

print(findClosestValueInBst(data['tree'], data['target']))
