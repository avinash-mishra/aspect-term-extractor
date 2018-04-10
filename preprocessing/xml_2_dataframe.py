# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pandas as pd

train_data = '../data/Laptops_Train_v2.xml'
test_data = '../data/Laptops_Test_Gold.xml'


class Xml2DataFrame:

    @staticmethod
    def parse_root(root):
        """Return pandas dataframe from given xml data"""
        data_list = []
        xml_data = dict()

        target_words = []
        for child in root:
            xml_data['id'] = child.attrib.get('id')
            # print(child.attrib)
            text = child.find('text').text.lower()
            xml_data['text'] = text
            # print(text)
            for aspectTerms in child.iter('aspectTerms'):
                aspectInfos = []
                for asp_term in aspectTerms:
                    aspectInfos.append(asp_term.attrib)
                    # print(asp_term.attrib)
                xml_data['aspect_info'] = aspectInfos
            data_list.append(xml_data)
            xml_data = {}

        return data_list

    def process_data(self, path):
        root = ET.parse(path).getroot()
        """ Initiate the root XML, parse it, and return a dataframe"""
        structure_data = self.parse_root(root)
        df = pd.DataFrame([[k.get('id'), k.get('text'), k.get('aspect_info')] for k in iter(structure_data)],
                          columns=['id', 'text', 'aspect_info'])
        print(df.head())
        return df


if __name__ == '__main__':
    xml2df = Xml2DataFrame()
    xml_dataframe = xml2df.process_data(test_data)
