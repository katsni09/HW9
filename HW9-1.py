# 1. Даний текстовий файл. Необхідно створити новий файл,
# який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
with open("input.txt", "w") as somefile:
    somefile.write(
        "At distant inhabit amongst by.\nAppetite welcomed interest the goodness boy not.\nEstimable education for disposing pronounce her.\nJohn size good gay plan sent old roof own.\nInquietude saw understood his friendship frequently yet.\nNature his marked ham wished.")
longerWord = []
with open("input.txt", "r") as input , open("output.txt", "w") as output:
    for inputLine in input:
        wordsForSplitting = inputLine.split()
        for oneSeparateWord in wordsForSplitting:
            if len(oneSeparateWord) >= 7:
                longerWord.append(oneSeparateWord)
    output.write(" ".join(longerWord))






