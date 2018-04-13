import pandas as pd


# convert into bio format
class BIO:

    def convert_into_bio(self, text, predicted_aspect_terms_list, common_words_list):
        text_list = text.split()
        # print(text_list)
        df = pd.DataFrame({'text': text_list, 'BIO': 'O'})

        bio_dict = self.bio_mapper(common_words_list=common_words_list, prediction=predicted_aspect_terms_list)
        bio_filtered_dict = self.filter_predicted_words(bio_dict)

        for item in bio_filtered_dict:
            final_list = self.matcher(text, item)
            if final_list[1] - final_list[0] == 0:
                df.at[final_list[0], 'BIO'] = 'B'
            else:
                df.at[final_list[0], 'BIO'] = 'B'
                for index in range(final_list[0] + 1, final_list[1] + 1):
                        df.at[index, 'BIO'] = 'I'

        print(df)
        return df

    def bio_mapper(self, common_words_list, prediction):
        bio_dict = dict()

        for i in range(len(common_words_list)):
            bio_dict[common_words_list[i]] = prediction[i]

        return bio_dict

    def matcher(self, text, word):
        split_word = word.split()
        split_text = text.split(word)

        if len(split_text) > 1:
            start = len(split_text[0].split())
            end = start + len(split_word) - 1
        return start, end

    def filter_predicted_words(self, _dict):

        final_list = []

        for key, value in _dict.items():
            if value == 1:
                final_list.append(key)

        return final_list;


if __name__ == '__main__':
    text = "The battery life is really good and its size is reasonable"
    x = BIO()
    prd = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    common_words = ['OS',
                    'Vista',
                    'Windows',
                    'Windows 7',
                    'applications',
                    'battery',
                    'battery life',
                    'carry',
                    'charge',
                    'cost',
                    'design',
                    'display',
                    'extended warranty',
                    'features',
                    'games',
                    'gaming',
                    'graphics',
                    'hard drive',
                    'keyboard',
                    'keys',
                    'look',
                    'memory',
                    'motherboard',
                    'mouse',
                    'operating system',
                    'performance',
                    'power',
                    'power supply',
                    'price',
                    'processor',
                    'program',
                    'programs',
                    'quality',
                    'runs',
                    'screen',
                    'service',
                    'shipping',
                    'size',
                    'software',
                    'speakers',
                    'speed',
                    'system',
                    'use',
                    'value',
                    'warranty',
                    'warrenty',
                    'weight',
                    'windows',
                    'work',
                    'works']

    x.convert_into_bio(text, prd, common_words_list=common_words)
