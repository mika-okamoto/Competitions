s = input()
t = 0
for i in range(len(s)):
    if s[i] == "Q":
        for j in range(i+1, len(s)):
            if s[j] == "A":
                for k in range(j+1, len(s)):
                    if s[k] == "Q":
                        t += 1

print(t)