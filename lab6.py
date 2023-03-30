# QnA DCCBBBA
f = open("text.txt","r")

positive=[]
neutral = []
negative=[]

for line in f:
    entries = line.split(",")
    entries[1] = int(entries[1].rstrip("\n"))
    #
    # print(entries[0])
    # print(entries[1])
    if entries[1] == 20:
        positive.append(entries[0])
    elif entries[1] == 0:
        neutral.append(entries[0])
    else:
        negative.append(entries[0])

tweet = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
tweetWords = tweet.split()
sentiment = 0
for word in tweetWords:
   if word in positive:
     sentiment+=20
   elif word in negative:
     sentiment-=10


print("The positive keywords are {}".format (positive))
print("The neutral keywords are {}".format(neutral))
print("The negative keywords are {}".format (negative))

f.close()

# problem 2
# text = open("text.txt", "r")
# myfile = open("myfile.txt", "w")
# line = text.read()  # added parentheses to call read() function
# words = line.split()
# for word in words:
#     print(word)  # removed unnecessary newline character
#     myfile.write(word + "\n")  # added newline character
# # Close the files
# text.close()
# myfile.close()