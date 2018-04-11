import nltk
from nltk.corpus import stopwords
from string import punctuation

class POSTagger:

    @staticmethod
    def pos_tagger(text):
        text = nltk.word_tokenize(text)
        stopwords_en = stopwords.words('english')
        stopwords_en_withpunct = set(stopwords_en).union(set(punctuation))
        text = [word for word in text if word not in stopwords_en_withpunct]
        tagged_pos_list = nltk.pos_tag(text)
        # print(tagged_pos_list)

        return tagged_pos_list

    @staticmethod
    def filter_pos_tag(tagged_text):
        final_text_list = []
        matching_tag = ['NN','NNS','NNP','NNPS','RB','RBR','RBS','JJ','JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ']

        for word, tag in tagged_text:
            final_text = []
            if tag in matching_tag:
                final_text.append(word)
                final_text_list.append((' '.join(final_text)))
        # print(final_text_list)
        return final_text_list


if __name__ == '__main__':
    x = POSTagger()
    k= x.pos_tagger("I am avinash and I am an Indian.")
    x.filter_pos_tag(k)