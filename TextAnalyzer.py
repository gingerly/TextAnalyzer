# Text Analyzer in Python

# Count the unique characters
def countChar(text, char):
    count = 0
    for c in text:
        if (c == char):
            count += 1
    return count

def findFreqTable(text):
    print("--- This is a frequency table ----")
    for ch  in "abcdefghijklmnopqrstuvwxyz":
        ch_count = float(countChar(text, ch))
        perc_ch = round(100*ch_count/len(text),2)
        print("{0} - {1}%".format(ch, perc_ch))

# Calling Area
filename = raw_input("Enter a file name:")

with open(filename) as f:
    text = f.read()


findFreqTable(text)
