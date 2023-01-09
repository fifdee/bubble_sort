to_sort = [
    (),
    (1, 2, 5, 3, 1, 7, 9, 1, 12, 83, 1, 5, 3, 2),
    (1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1),
    (2, 2, 2, 2),
    (1, 2),
    (2, 1)]


def my_sorted(input_sequence):
    result = list(input_sequence)
    while True:
        changes = 0
        for i in range(0, len(result)):
            if i < len(result) - 1:
                if result[i + 1] < result[i]:
                    this_val = result[i]
                    next_element_val = result[i + 1]

                    result[i + 1] = this_val
                    result[i] = next_element_val

                    changes += 1
        if changes == 0:
            break
    return result


for seq in to_sort:
    print(my_sorted(seq))
