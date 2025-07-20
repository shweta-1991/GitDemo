with open("text.txt","r") as reader:
    content=reader.readlines()
    list1=reversed(content)
    with open("text.txt","w") as writer:
        for line in list1:

            writer.write(line)
            print(line)




