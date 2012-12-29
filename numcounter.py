s = "13715314919397913275511122340811633276551212434879751951"

numarr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for char in s:
    numarr[int(char)] += 1

print(numarr)
