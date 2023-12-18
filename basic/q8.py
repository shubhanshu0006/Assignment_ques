def count_frequency(input_list):
    frequency_dict = {}
    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element]+=1
        else:
            frequency_dict[element]=1
    return frequency_dict

my_list = [1, 2, 3, 1, 2, 4, 5, 1, 2, 6]
result = count_frequency(my_list)
print(result)

