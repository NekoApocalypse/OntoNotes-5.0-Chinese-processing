import os
import os.path
import re
import glob
import numpy as np
from collections import Counter

# Get full path to the directory of python file
dir_path = os.path.dirname(os.path.realpath(__file__))
onto_50_path = dir_path+'/dataset/OntoNotes5_0_annotations'
genre_list = ['bc', 'bn', 'mz', 'nw', 'tc', 'wb']
primary_type = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART',
             'LAW', 'LANGUAGE']
secondary_type = ['DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']
interest_type = ['PERSON']
# 11 Primary types, 7 Secondary types

# Get current cwd
# cwd = os.getcwd()


def potential_relation(str, window_size):
    ''' Return a numpy matrix of relation counts between types '''
    in_window = [] # ((word, type),num)
    sentence_list = []
    relation_matrix = np.zeros([11,11],dtype=int)
    for nu, word in enumerate(str):
        while in_window and (nu-in_window[0][1]>=window_size):
            in_window.pop(0)
        if word[1] in primary_type:
            for (pre_word, pnu) in in_window:
                relation_matrix[primary_type.index(pre_word[1])][primary_type.index(word[1])] += 1
                if word[1] in interest_type and pre_word[1] in interest_type:
                    sentence_list.append(str[pnu:nu+1])
            in_window.append((word,nu))
    return relation_matrix, sentence_list


def sentence_slice(str):
    ''' Slice a sentence into (word, type) list form '''
    if re.search(r'(\<DOC)|(\<\/DOC)', str) is not None:
        return []
    sliced = (re.sub(r'X T', r'X_T', str)).split()
    # return [entity_slice(x) for x in sliced]
    start = None
    type = ''
    buffer = ''
    word_list = []
    for segment in sliced:
        if start is None:
            start = re.search(r'TYPE=\"(.+?)\"', segment)
            if start is None:
                word_list.append((segment, ''))
                continue
            type = start.group(1)
            segment = re.sub(r'\<ENAMEX_TYPE=".+?"\>','', segment)
            end = re.search(r'\<\/ENAMEX\>', segment)
            if end is not None:
                word_list.append((re.sub(r'\<\/ENAMEX\>', '', segment), type))
                start = None
            else:
                buffer = segment
        else:
            end = re.search(r'\<\/ENAMEX\>', segment)
            if end is not None:
                segment = re.sub(r'\<\/ENAMEX\>', '', segment)
                word_list.append((buffer + ' ' + segment, type))
                start = None
            else:
                buffer += ' ' + segment
    return word_list


def dict_to_md(dict, output_file, order=None, header1='Keys', header2='Values', override=False, encoding='utf-8'):
    ''' Convert a {A: B} dictionary into a mark-down table and write to file '''
    try:
        if not override and os.path.isfile(output_file):
            raise FileExistsError('File already exists. Will not override.')
    except FileExistsError as err:
        print('Error:', err)

    with open(output_file, 'w+', encoding='tf8') as f:
        print('|'+header1+'|'+header2+'|', file=f)
        print('|---|---|', file=f)
        if order is None:
            for key, value in dict.iteritems():
                print('|', key, '|', value,'|', file=f)
        else:
            for key in order:
                print('|', key, '|', dict[key],'|', file=f)


def read_entity(path_to_file, encoding='utf-8'):
    ''' Find all marked named entity in file '''
    pattern = re.compile(r'\<.+?\/ENAMEX\>')
    entity_list = []
    with open(path_to_file, encoding=encoding) as f:
        for line in f:
            candidate_list = pattern.findall(line)
            entities = [entity_slice(item) for item in candidate_list]
            entity_list.extend(entities)
    return entity_list


def entity_collect():
    dir =  onto_50_path + '/nw'
    print(os.listdir(dir))
    entity_list = []
    file_list = glob.glob(dir+'/**/*.name', recursive=True)
    print('Total number of files: ', len(file_list))
    for file in file_list:
        entity_list.extend(read_entity(file))
    print('Total number of Entities: ', len(entity_list))
    category = Counter(x[1] for x in entity_list)
    dict_to_md(category, 'category.md', order=primary_type, override=True)


if __name__=='__main__':
    dir = onto_50_path + '/nw'
    file_list = glob.glob(dir+'/**/*.name', recursive = True)
    relation_matrix = np.zeros([11,11], dtype=int)
    occurrence_list = []
    for file in file_list:
        # print(file)
        with open(file, encoding='utf-8') as f:
            article = []
            for line in f:
                article.extend(sentence_slice(line))
            sub_matrix, lr = potential_relation(article, 10)
            relation_matrix += sub_matrix
            occurrence_list.extend(lr)
            # print(article)
    print(relation_matrix)
    with open('occurrence_sample.txt', 'w+', encoding='utf-8') as f:
        for sentence in occurrence_list:
            print(sentence, file=f)
