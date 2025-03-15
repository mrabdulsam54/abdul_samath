from itertools import combinations, permutations
import enchant
repeat_action = True
while repeat_action is True:
    l = map(str, input("Type the letters separated by space! ").split(" "))
    n = int(input("What is the combination count? "))
    r = permutations(l, n)
    check = enchant.Dict('en_US')
    unique_words = []
    for i in r:
        word = "".join(i)
        if check.check(word) is True:
            unique_words.append(word)
        else:
            pass
    unique_words = set(unique_words)
    print(f"Your possible word count can be {len(unique_words)} and listed below!")
    for j in unique_words:
        print(j.upper())
    if input("Do you want to continue? y/n ") == "n":
        repeat_action = False
    else:
        continue
