with open("text.txt","r") as reader:
    content1=reader.readlines()
    list1=reversed(content1)
    with open("text.txt","w") as writer:
        for line in list1:

            writer.write(line)
            print(line)




