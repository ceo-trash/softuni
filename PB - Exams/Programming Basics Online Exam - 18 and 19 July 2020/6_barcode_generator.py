start = input()
end = input()

first_start = int(start[0])
second_start = int(start[1])
third_start = int(start[2])
fourth_start = int(start[3])

first_end = int(end[0])
second_end = int(end[1])
third_end = int(end[2])
fourth_end = int(end[3])


for num_1 in range(first_start, first_end + 1):

    for num_2 in range(second_start, second_end + 1):

        for num_3 in range(third_start, third_end + 1):

            for num_4 in range(fourth_start, fourth_end + 1):

                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')





# start = input()
# end = input()
#
#
# first_start = int(start / 1000)
# second_start = int((start / 100) % 10)
# third_start = int((start / 10) % 10)
# fourth_start = int(start % 10)
#
# first_end = int(end / 1000)
# second_end = int((end / 100) % 10)
# third_end = int((end / 10) % 10)
# fourth_end = int(end % 10)
#
#
#
#
# for num_1 in range(first_start if first_start % 2 != 0 else first_start + 1, first_end + 1, 2):
#
#     for num_2 in range(second_start if second_start % 2 != 0 else second_start + 1, second_end + 1, 2):
#
#         for num_3 in range(third_start if third_start % 2 != 0 else third_start + 1, third_end + 1, 2):
#
#             for num_4 in range(fourth_start if fourth_start % 2 != 0 else fourth_start + 1, fourth_end + 1, 2):
#
#                     print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')
