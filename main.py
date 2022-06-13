# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(file_content):
    # [assignment] Add your code here
    with open(file_content) as f:
        content = f.read()
        return content


def count_words(text):
    text = read_file_content('story.txt').split
    counts = dict()
    # [assignment] Add your code here

    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(count_words('story.txt'))