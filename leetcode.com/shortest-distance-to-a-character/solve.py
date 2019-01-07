def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    result = [1000000 for _ in S]
    if S[0] == C:
        result[0] = 0
    for i in range(1, len(S)):
        if S[i] == C:
            result[i] = 0
            backIndex = i-1
            backValue = 1
            while result[backIndex] > backValue:
                result[backIndex] = backValue
                backIndex -= 1
                backValue += 1
        else:
            result[i] = result[i-1] + 1
    return result

print(shortestToChar(False, "loveleetcode", 'e'))
