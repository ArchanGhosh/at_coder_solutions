def solve(s):
    words = {"maerd": 5, "remaerd": 7, "esare": 5, "resare": 6}

    i = 0
    while i < len(s):
        for word in words:
            if s.startswith(word, i):
                i += words[word]
                break
        else:
            print("NO")
            return

    print("YES")
s = input()
solve(s[::-1])
