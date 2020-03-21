'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):

#     # append counter to the end of the word
#     try:
#         int(word[len(word) - 1])
#     except:
#         word = word + str(0)
    
#     # base case
#     try:
#         int(word)
#         return int(word)
#     except:
#         pass
        
#     if word[0:2] == "th":
#         # If the first two characters of the word is "th",
#         # then remove from the word and increase the count
#         count = 0
#         int_start_index = 0

#         # Get the count part of the word and increament
#         for i in reversed(range(len(word))):
#             try:
#                 int(word[i])
#             except:
#                 count = int(word[i+1:])
#                 int_start_index = i + 1
#                 break

#         count += 1
#         return count_th(word[2:int_start_index] + str(count))
#     else:
#         # If the first two character of the word is not "th",
#         # then remove the first character from the word
#         return count_th(word[1:])
    
def count_th(word):
    if len(word) < 2:
        return 0
    elif word == "th":
        return 1
    elif "th" in word:
        start_index = word.find("th")
        return 1 + count_th(word[start_index + 2 : ])
    else:
        return 0

    


    
print(count_th("asthahtasth"))
