


def longestCommonPrefix(strs):
    def frequent(list):

        return (max(set(list), key=list.count))

    ans = ""
    testlist = []
    testset = {}
    for i in strs:
        testlist.append(i[0:1])
    testset = set(testlist)
    if len(testset) == len(testlist):
        return ("")

    word_length = len(min(strs))

    for i in range(len(strs)):
        strs[i] = strs[i][0:word_length]
    templist = []
    while len(templist) == len(set(templist)):

        for i in range(word_length):

            for word in strs:
                templist.append(word[0:i + 1])
            print(templist)
        templist.clear()

    return ans


print(longestCommonPrefix(["flower", "flow", "flight"]))