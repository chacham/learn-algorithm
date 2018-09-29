def solution(words):
    w = {}
    for word in words:
        key = word[0]
        if key not in w:
            w[key] = []
        w[key].append(word)

    result = 0
    while w:
        k, v = w.popitem()
        if len(v) == 1:
            result += len(k)
        else:
            for word in v:
                key = word[:len(k)+1]
                if key not in w:
                    w[key] = []
                w[key].append(word)
    return result

if __name__ == "__main__":
    wordsList = [
        ["go", "gone", "guild"],
        ["abc", "def", "ghi", "jklm"],
        ["word", "war", "warrior", "world"],
    ]
    for words in wordsList:
        print(solution(words))
