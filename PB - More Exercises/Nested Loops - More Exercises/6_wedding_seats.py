sector_simbols = input()
number_rows_sector_one = int(input())
number_space_odd_row = int(input())

starting_sector = ord('A')
ending_sector = ord(sector_simbols)
starting_place = ord('a')
additional_row = 0
additional_row_odd = 2
total_seats = 0


for sector in range(starting_sector, ending_sector + 1):
    additional_row += 1

    for row in range(1, number_rows_sector_one + additional_row):

        if row % 2 != 0:
            for place in range(starting_place, starting_place + number_space_odd_row):
                print(f'{chr(sector)}{row}{chr(place)}')
                total_seats += 1

        else:
            for place in range(starting_place, starting_place + number_space_odd_row + additional_row_odd):
                print(f'{chr(sector)}{row}{chr(place)}')
                total_seats += 1

print(total_seats)






# import string
#
# sector_simbols = input()
# number_rows_sector_one = int(input())
# number_space_odd_row = int(input())
#
# alphabet_list_lower = string.ascii_lowercase
# alphabet_list_up = string.ascii_uppercase
# sector_one = alphabet_list_up.index(sector_simbols)
# checking_letters = alphabet_list_up[:sector_one + 1]
# even_rows = number_space_odd_row + 1
# counter_operation = 0
# add_row = 0
#
# for letter in checking_letters:
#     even_rows += 1
#     add_row += 1
#
#     for row in range(1, number_rows_sector_one + add_row):
#         added_rows = 0
#         even_rows_count = 0
#
#         for possition in alphabet_list_lower:
#
#             if added_rows > even_rows:
#                 break
#
#             if letter == "A":
#
#                 if row % 2 == 0 and even_rows_count < even_rows:
#                     print(f"{letter}{row}{possition}")
#                     even_rows_count += 1
#                     counter_operation += 1
#
#             else:
#                 if row % 2 == 0 and even_rows_count < even_rows - add_row + 1:
#                     print(f"{letter}{row}{possition}")
#                     even_rows_count += 1
#                     counter_operation += 1
#
#             if row % 2 != 0 and number_space_odd_row > added_rows:
#                 print(f"{letter}{row}{possition}")
#                 counter_operation += 1
#             added_rows += 1
#
# print(counter_operation)
