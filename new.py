# lets assume that we have an array of cuss words that have to be looked in the tweets
# the tweets are kept in the a different file called 'test.txt'
#also i have taking some cuss words instead of racial slurs because thats what people face on the internet more than racial slurs.
#kindly dont mind the words "they are just for the programm". "i do not cuss in real life"
arr = ['f*ck','sh*t','bi*ch','m*','b*',"a**hole"] 
f = open('test.txt', 'r')
for i in f:
    # print the tweet from the file
    print(i, end='')
    words = i.split()
    length = len(words)
    # after separating all the words in an array we print the length of the save and print array
    print(length)
    count = 0
    # create a count and check every word in our new array with every profanity in the arr
    for x in range(length):
        words[x] = words[x].replace(',',"")
        for y in range(len(arr)):
            if words[x] == arr[y]:
                count+=1
    print(count)
    # calculate the percentage of the profanity 
    degree = count/length
    print(degree*100,"%")
    print()
f.close()

        
