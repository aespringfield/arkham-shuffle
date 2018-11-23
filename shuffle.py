import random
import sys
import copy

def buildPool(stacks):
    pool = []
    for stack in stacks:
        for i in range(stack['size']):
            pool.append({
                'classname': stack['name'],
                'position': i
            })
    return pool

def buildDeck(pool, deckSize):
    return random.sample(pool, deckSize)
    
def sortByCardClass(deck):
    sortedDeck = {}
    for card in deck:
        if card['classname'] in sortedDeck:
            sortedDeck[card['classname']].append(card['position'])
        else:
            sortedDeck[card['classname']] = [card['position']]
    for classname in sortedDeck:
        sortedDeck[classname].sort()
    return sortedDeck

def createDeckFromStacks(stacks, deckSize):
    pool = buildPool(stacks)
    deck = buildDeck(pool, deckSize)
    return sortByCardClass(deck)

def createDictFromArgs(args):
    keys = args[0::2]
    values = args[1::2]
    argsDict = {}
    for i, key in enumerate(keys):
        try:
            argsDict[key] = int(values[i])
        except ValueError:
            raise ValueError('Must provide value')
    return argsDict

def getDeckSize(argsDict):
    try:
        deckSize = argsDict['deckSize']
    except KeyError:
        raise KeyError('Must provide \'deckSize\' argument')
    return deckSize
            
def getStackSizes(argDict, classNames):
    stackSizes = {}
    for className in classNames:
        if className in argsDict:
            stackSizes[className] = argsDict[className]
    if not stackSizes:
        raise ValueError('Must provide at least one stack')
    return stackSizes

def createStacks(stackSizes):
    stacks = []
    for className in stackSizes:
        stacks.append({
            'name': className,
            'size': stackSizes[className]
        })
    return stacks

def printDeck(deck):
    for classname in deck:
        print("{}: {}".format(classname, deck[classname]))

def subtractDeckFromStacks(deck, stacks):
    newStacks = copy.copy(stacks)
    for stack in newStacks:
        className = stack['name']
        if className in deck:
            stack['size'] -= len(deck[className])
    return newStacks

def printNewStacks(newStacks):
    for stack in newStacks:
        print("{}: {}".format(stack['name'], stack['size']))


args = sys.argv[1:]
classNames = ['Survivor', 'Rogue', 'Guardian', 'Mystic', 'Seeker', 'Neutral']
argsDict = createDictFromArgs(args)
deckSize = getDeckSize(argsDict)
stackSizes = getStackSizes(argsDict, classNames)
stacks = createStacks(stackSizes)
deck = createDeckFromStacks(stacks, deckSize)
newStacks = subtractDeckFromStacks(deck, stacks)

printDeck(deck)
print('\n**** Adjusted stacks ****\n')
printNewStacks(newStacks)
