def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    result = [1000000 for _ in S]
    if S[0] == C:
        result[0] = 0
    if S[-1] == C:
        result[-1] = 0
    for i in range(1, len(S)):
        if S[i] == C:
            result[i] = 0
        else:
            result[i] = min(result[i-1] + 1, result[i])
    for i in range(len(S) - 2, -1, -1):
        if S[i] == C:
            result[i] = 0
        else:
            result[i] = min(result[i+1] + 1, result[i])
    return result

print(shortestToChar(False, "loveleetcode", 'e'))
