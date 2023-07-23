def toggle_hat_status(cats, round_number):
    for i in range(round_number - 1, len(cats), round_number):
        cats[i] = 1 - cats[i]


def find_cats_with_hats(num_cats):
    cats = [0] * num_cats

    for round_number in range(1, num_cats + 1):
        toggle_hat_status(cats, round_number)

    cats_with_hats = [i + 1 for i, status in enumerate(cats) if status == 1]
    return cats_with_hats


num_cats = 100
cats_with_hats = find_cats_with_hats(num_cats)
print("Cats with hats at the end:", cats_with_hats)
