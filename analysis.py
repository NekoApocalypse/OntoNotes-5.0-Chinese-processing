import os
import re
import glob
from collections import Counter

# Get full path to the directory of python file
dir_path = os.path.dirname(os.path.realpath(__file__))
onto_50_path = dir_path+'/dataset/OntoNotes5_0_annotations'
genre_list = ['bc', 'bn', 'mz', 'nw', 'tc', 'wb']

# Get current cwd
# cwd = os.getcwd()

def slice_entity(str):
    word = re.search(r'(?<=\>).+?(?=\<)', str).group(0)
    type = re.search(r'(?<=\=\").+?(?=\")', str).group(0)
    return (word, type)

def read_entity(path_to_file, encoding='utf-8'):
    pattern = re.compile(r'\<.+?\/ENAMEX\>')
    entity_list = []
    with open(path_to_file, encoding=encoding) as f:
        for line in f:
            candidate_list = pattern.findall(line)
            entities = [slice_entity(item) for item in candidate_list]
            entity_list.extend(entities)
    return entity_list

if __name__=='__main__':
    dir =  onto_50_path + '/nw'
    print(os.listdir(dir))
    entity_list = []
    file_list = glob.glob(dir+'/**/*.name', recursive=True)
    print('Total number of files: ', len(file_list))
    for file in file_list:
        entity_list.extend(read_entity(file))
    print('Total number of Entities: ', len(entity_list))
    category = Counter(x[1] for x in entity_list)
    print(category)
