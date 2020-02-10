from functools import reduce


def printList(list):
    print(" ".join(str(x) for x in list))


def check(num, answer_list):
    if (num not in answer_list):
        hangman.append(num)
    pos = 0
    score = 0
    # print(answer_list)
    while (num in answer_list):
        pos = pos+answer_list.index(num)+1
        hangman[pos-1] = num
        answer_list = answer_list[answer_list.index(num)+1:]
        score += 1
        # print("Pos :", pos)
        # print(answer_list)
        # print(hangman)
    scores.append(score)
    printList(hangman)


# check(9, answer_list)
# check(6, answer_list)
# check(7, answer_list)
# check(2, answer_list)
# check(4, answer_list)

answer = input('Input Problem : ')
answer_list = [int(i) for i in answer.split(' ')]
print(answer_list)
# answer_list = [9, 9, 4, 2, 2, 4, 7, 7, 9, 6, 6, 4]
# answer_list = [1, 2, 3, 4, 5, 1, 2, 3, 3, 3, 1, 2]
hangman = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
scores = []
for i in range(5):
    guess_number = eval(input('Guess number : '))
    check(guess_number, answer_list)
    print("Score : ", reduce(lambda x, y: x+y, scores))
