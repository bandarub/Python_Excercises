def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    number_dict = {}

    for i in range(20):
        number_dict[i] = ones[i]
    
    for i in range(20, 100):
        ten_part = i // 10
        ones_part = i % 10 
        if ones_part == 0:
            number_dict[i] = tens[ten_part]
        else:
            number_dict[i] = tens[ten_part] + "-" + ones[ones_part]

    return number_dict
    

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

