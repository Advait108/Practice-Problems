

#takes list input and returns longest common prefix
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return (strs[0])
    if len(set(strs)) == 1:
        return strs[0]
    testlist = []
    for i in strs:
        testlist.append(i[0:1])
    testset = set(testlist)

    if len(testset) > 1:
        return ("")

    ans = ""
    for i in range(len(min(strs))):
        temp1 = []
        temp2 = []
        for x in strs:
            temp1.append(x[0:i + 1])
            if i < len(min(strs)) + 1:
                temp2.append(x[0:i + 2])

        if len(set(temp1)) == 1:
            if len(set(temp2)) != 1:
                return temp1[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))