def reverse_string(str):
    if not str or len(str) < 2:
        return "hmm that's not good"
    backwards = []
    totalItems = len(str)
    for i in range(totalItems - 1, -1, -1):
        backwards.append(str[i])

    return ''.join(backwards)

    # return str[::-1] Alternative way to reverse a string

print(reverse_string("Hello, World!"))