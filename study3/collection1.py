def wirteFile():
    file = open("data.json", "a")
    input("start")
    while True:
        word = input("enter word(',' to quit)")
        if word != '.':
            file.write(word)
        else:
            break
    file.close()


wirteFile()
print([x ** 2 for x in range(6)])

print(max(len(x.strip()) for x in open("data.json")))
