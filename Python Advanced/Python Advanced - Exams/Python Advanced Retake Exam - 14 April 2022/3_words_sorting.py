def words_sorting(*args):
    output, result = "", {}
    for word in args:
        result[word] = result.get(word, 0) + sum([ord(x) for x in word])
    if sum(result.values()) % 2 != 0:
        for p_word, p_value in sorted(result.items(), key=lambda x: -x[1]):
            output += f"{p_word} - {p_value}\n"
    else:
        for p_word in sorted(result):
            output += f"{p_word} - {result[p_word]}\n"
    return output

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))