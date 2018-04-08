from textblob import TextBlob
import sys


def main():
    blob = TextBlob('I like the pizza at the restaurant')
    tokens = list(blob.words)
    word = []
    sent = []
    c = 0
    i = 0
    for words, pos in blob.tags:
        if pos == 'JJ' or pos == 'NN' or pos == 'JJR' or pos == 'NNS':
            word.append(words)
    if len(word) >= 2:
        for i in range(len(word)):
            if len(word) >= 2:
                print(i)
                firstw = word[0]
                secw = word[1]
                word.remove(firstw)
                word.remove(secw)
                findx = tokens.index(firstw)
                lindx = tokens.index(secw)
                sent.append(' '.join(tokens[findx:lindx + 1]))

    print(sent)
    print(tokens)
    print("Sentence and polarity")
    for sentence in sent:
        print(sentence, TextBlob(sentence).polarity)


if __name__ == '__main__':
    main()