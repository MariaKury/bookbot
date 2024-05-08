def main():
    book_path = "books/frankenstein.txt"
    text = getTextBook(book_path)
    numWords = getNumWords(text)
    numChars = getNumChars(text)
    numChars = formatChars(numChars)
    printReport(book_path, numWords, numChars)

def getTextBook(path):
    with open(path) as f:
        return f.read()

def getNumWords(text):
    words = text.split()
    return len(words)

def getNumChars(text):
    chars = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in chars:
                chars[letter] += 1   
            else:
                chars[letter] = 1
    return chars

def formatChars(chars):
    lsChars = [{"char": k, "num": v} for k, v in chars.items()]
    filteredChars = filterChars(lsChars)
    filteredChars.sort(reverse=True, key=sort_on)
    return filteredChars

def filterChars(chars):
    ls = []
    
    for char in chars:
        if char["char"].isalpha():
            ls.append(char)

    return ls        

    
def sort_on(dict):
    return dict["num"]
        

def printReport(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for char in chars:
        print(f"The {char["char"]} character was found {char["num"]} times")
    print("--- End report ---")
    
main()