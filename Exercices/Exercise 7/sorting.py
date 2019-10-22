def parseTextFile(filename):
    filereader = open(filename)
    textArray = []
    for textLine in filereader:
        newTextLine = textLine.strip('\n')
        textArray.append(newTextLine)

    return textArray


'''
Function parses the textfile into something that is directly compatible with sorting

method: filereader

takes:
filename:string:name of the file that shall be parsed

yields:
unsorted textArray with each line from the textfile without linebreak
'''


def insertionSort(textFile):
    textArray = parseTextFile(textFile)

    for index in range(1, len(textArray)):
        currentValue = textArray[index]  # arne
        position = index  # nummer

        while position > 0 and compareText(textArray[position - 1], currentValue):
            textArray[position] = textArray[position - 1]
            position = position - 1

        textArray[position] = currentValue

    print(textArray)


'''
Function that sorts the textArray by using insertion sort

takes:
textFile:string

prints:
Sorted textArray
'''


def compareText(textA, textB):
    if len(textA) > len(textB):
        return True
    elif len(textA) == len(textB):
        if textA > textB:
            return True
        else:
            return False
    else:
        return False


'''
Function that compares two text strings, and returns true or false
It first checks their length, then their lexicographically order if their length is equivalent 

takes:
textA:string:first string to compare
textB:string: ssecond string to compare

yields:
if textA > text B:
    True
if textA < textB:
    False

'''


def main():
    insertionSort("listofRandomWords.txt")


if __name__ == "__main__":
    main()

'''
Function main()
used to start the sorting algorithm, by providing a textFile name string to the sorting algorithm

Text file format:
word1
word2
etc...

'''