
ALPHABET_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class StringUtil:

    def count_digits(input):

        sum = 0
        for char in input:
            if char != " ":
                sum = sum + int(char)

        return sum

    def get_life_path(input_string):

        print("Input String: " + input_string)
        month_str = input_string[0] + input_string[1]
        month_num = StringUtil.count_digits(month_str)

        day_str = input_string[3] + input_string[4]
        day_num = StringUtil.count_digits(day_str)

        year_str = input_string[6] + input_string[7] + input_string[8] + input_string[9]
        year_num = StringUtil.count_digits(year_str)

        if year_num > 10:
            year_num = StringUtil.count_digits(str(year_num))

        print("Month: " + str(month_num))
        print("Day: " + str(day_num))
        print("Year: " + str(year_num))
        print("Life Path Number: " + str(
            month_num +
            day_num +
            year_num
        ))

    def get_personality_number(input_string, msg):

        num = StringUtil.count_digits(input_string)

        if num >= 10:
            num2 = StringUtil.count_digits(str(num))
            print(msg + ": " + str(num2))
            return num2

        else:
            print(msg + ": " + str(num))
            return num

    def set_destiny_number_alpha_dictionary():

        val = 1
        dict = {}
        for char in ALPHABET_LIST:
            if val % 9 == 0:
                dict[char] = val
                val = 0
            else:
                dict[char] = val
            val = val + 1

        return dict