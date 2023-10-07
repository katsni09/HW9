# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

with open("inputHW92.txt", "w") as somefile:
    somefile.write(
        "Death weeks early had their and folly timed put. Hearted forbade on an village ye in fifteen. Age attended betrayed her man raptures laughter.")
longerWord = []
with open("inputHW92.txt", "r") as input:
    for inputLine in input:
        wordsForSplitting = inputLine.split()
    countTheWords = len(wordsForSplitting)
    print(countTheWords)
