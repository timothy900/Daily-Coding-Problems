import random

# number of different trees there can be
treeVariety = 5


# generating a list of trees
def treesList(listLength):
    trees = []
    for i in range(listLength):
        trees.append(random.randint(1, treeVariety))
    return trees


# find longest part of list consisting of 2 different trees
def findLongest(x):
    # generate a list of trees of length x
    trees = treesList(x)

    listOfLists = []
    currentList = []

    # two different trees
    tree1 = trees[0]
    tree2 = -1

    for i in trees:
        if not i == tree1:
            tree2 = i
            break

    # check every tree
    for tree in trees:
        nextTree = trees[tree+1]
        if not nextTree == tree1 or not nextTree == tree2:
            if tree == tree1:
                tree2 = nextTree
            else:
                tree1 = nextTree
            # store in listOfLists
            listOfLists.append(currentList)
            # restart count
            currentList.clear()
        # continue count
        else:
            currentList.append(tree)
        return listOfLists


print(findLongest(10))
