"""
AoCd Day 8
https://adventofcode.com/2021/day/8
"""
import sys

def get_easy_numbers(data):
    ""
    lines = [line.split('|')[1].strip() for line in data]
    len_list = [[len(word) for word in l.split()] for l in lines]
    num_list = [2,4,3,7]
    easy_count = 0
    for line in len_list:
        for item in line:
            if item in num_list:
                easy_count += 1
    return easy_count

def get_map_dict(line):
    ""
    word_num_dict = {}
    for word in line.split():
        word_num_dict[word] = set(word)
    
    number_charset_dict = {}
    #2
    for key,value in word_num_dict.items():
        if len(key) == 2:
            number_charset_dict[1] = value
            break
    #7
    for key, value in word_num_dict.items():
        if len(key) == 3:
            number_charset_dict[7] = value
            break
    #4
    for key, value in word_num_dict.items():
        if len(key) == 4:
            number_charset_dict[4] = value
            break
    #8
    for key, value in word_num_dict.items():
        if len(key) == 7:
            number_charset_dict[8] = value
            break
    #3
    for key,value in word_num_dict.items():
        if len(key) == 5 and number_charset_dict[1].issubset(value):
            number_charset_dict[3] = value
            break
    #6
    for key,value in word_num_dict.items():
        if len(key) == 6 and not number_charset_dict[1].issubset(value):
            number_charset_dict[6] = value
            break
    #9           
    for key, value in word_num_dict.items(): 
        if len(key) == 6:
            if number_charset_dict[3].issubset(value):
                number_charset_dict[9] = value
                break
    #0
    for key, value in word_num_dict.items(): 
        if (len(key) == 6)\
          and (value != number_charset_dict[9])\
          and (value != number_charset_dict[6]):
                number_charset_dict[0] = value
                break
    #1 bottom
    for key,value in word_num_dict.items():
        one_bottom_seg = number_charset_dict[1].intersection(number_charset_dict[6])
        break 
    #2
    for key, value in word_num_dict.items():
        if (len(key) == 5) and not (one_bottom_seg.issubset(value)):
            number_charset_dict[2] = value
            break
    #5 
    one_upper_seg = number_charset_dict[1] - one_bottom_seg
    for key, value in word_num_dict.items():
        if (len(key) == 5) and not (one_upper_seg.issubset(value)):
            number_charset_dict[5] = value
            break

    return number_charset_dict

def get_display_number(line,map_dict):
    display_number = []
    for word in dd.split():
        for key, value in map_dict.items():
            if set(word) == value:
                display_number.append(key)
    display_number = int("".join(map(str,display_number)))
    return display_number
###
with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

encode_data = [line.split('|')[0].strip() for line in data]
decode_data = [line.split('|')[1].strip() for line in data]

number_collector_list = []

for ed, dd in zip(encode_data, decode_data):
    map_dict = get_map_dict(ed)
    number = get_display_number(dd,map_dict)
    number_collector_list.append(number)

result_1 = get_easy_numbers(data)
result_2 = sum(number_collector_list)

print(f"res_1={result_1}\nres_2={result_2}")
