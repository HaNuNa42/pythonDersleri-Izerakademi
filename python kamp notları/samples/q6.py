def Q1(numberList):
    sum = 0
    for number in numberList:
        sum = sum + number
    return sum


def Q2(numberList):
    mul = 1
    for number in numberList:
        mul = mul * number
    return mul


def Q3(numberList):
    max = numberList[0]
    for number in numberList:
        if number > max:
            max = number
    return max


def Q4(numberList):
    min = numberList[0]
    for number in numberList:
        if number < min:
            min = number
    return min

def Q5(wordList):
    counter = 0
    for word in wordList:
        if len(word) >2 and word[0]== word[-1]:
            counter+=1
    return counter


def Q6(n,str):
    wordList = []
    textList = str.split(" ")
    for text in textList:
        if len(text) > n:
            wordList.append(text)
    return wordList


print("sum: {0}".format(Q1([1, 2, -8])))
print("mul: {0}".format(Q2([1, 2, -8])))
print("max: {0}".format(Q3([1, 2, -8])))
print("min: {0}".format(Q4([1, 2, -8])))
print("Counter : {0}".format(Q5(["abc", "xyz", "aba", "1221"])))
print("long words : {0}".format(Q6(3, "the quick brown fox jumps over the lazy dog")))