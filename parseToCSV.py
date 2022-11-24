import numpy as np
import pandas as pd
import re
from analyzePDF import analyzePDF
FILENAME = 'file.pdf'

def analyze_pdf(file):
    result = analyzePDF(file)
    my_list = [] 
    for i in result.values(): 
        my_list.append(i)
    return my_list

def distribute_data_to_label(analyzed_list):
    analyzed_list_unwrap = []
    column_attributes = []
    column_attributes_corr_val = []
    for i in analyzed_list[0]:
        analyzed_list_unwrap.append(i)

    for key, val in analyzed_list_unwrap[0].items():
        column_attributes.append(key)
        column_attributes_corr_val.append(val)
    
    analyzed_list_unwrap[0].pop('version')
    analyzed_list_unwrap[0].pop('filename')
    analyzed_list_unwrap[0].pop('header')
    
    final_dict = dict(analyzed_list_unwrap[0])
    del column_attributes[0:3]
    del column_attributes_corr_val[0:3]
    
    print(final_dict)   
    print(column_attributes)
    print(column_attributes_corr_val)

    return final_dict, column_attributes, column_attributes_corr_val


def main():
    filename = [FILENAME]
    result = analyze_pdf(filename)
    dictionary, columns, values = distribute_data_to_label(result)
    # print(result)


if __name__ == '__main__':
    main()