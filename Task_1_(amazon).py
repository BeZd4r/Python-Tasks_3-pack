from random import randint

temp_lst = [randint(-50,50) for _ in range(100)]
result = {}

for temp_index in range(len(temp_lst)):

    temp = temp_lst[temp_index]
    days_to = 0

    for next_temp in temp_lst[temp_index:]:
        if temp < next_temp:
            break
        days_to += 1
    
    result[f'day_{temp_index+1}'] = {'temperature' : temp, "hotter_temperature"  : next_temp, 'days_to' : days_to}

for key, value in result.items():
    print(key)
    for value_key,value_value in value.items():
        print(value_key, value_value)
    print() 