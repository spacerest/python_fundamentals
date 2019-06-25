'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
file = 'words.txt'
with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() # creates a list
    words.sort(key=len)
    print(words[:10])
    min_words_list = []
    max_words_list = []
    #print(words[0])# check to see first word
    #print(type(words[0])) #check to see the type its a string
    print(words[len(words)-1]) #check to see the last word
    first = int(len(words[0]))  # smallest word should be at the front due to the sort
    last = int(len(words[len(words)-1])) # largest word should be at the back due to the sort
    for word in words: #creating a new list for all small words with the same length
        if len(word) == first:
            min_words_list.append(word)
            #print(word, end=" ")
        if len(word) == last: #creating a new list for all large words with the same length
            max_words_list.append(word)
            print(word, end=" ")
    print()# to break for a new line
    print('The file ' + file + ' has ' + str(len(words)) + " words.")


    print(min_words_list)
    print(max_words_list)
    print(len(min_words_list))
    print(len(max_words_list))

    print(min_words_list[0].capitalize() + ' is one of the shortest word containing a length of ' + str(len(min_words_list[0])) + ' characters.')
    print(max_words_list[0].capitalize() + ' is one of the longest word containing a length of ' + str(len(max_words_list[0])) + ' characters.')
