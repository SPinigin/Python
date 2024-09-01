def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


def get_user_input():
    arr = []
    print("Введите 10 уникальных чисел от 0 до 100:")

    while len(arr) < 10:
        try:
            num = int(input(f"Введите число {len(arr) + 1}: "))
            if 0 <= num <= 100:
                if num not in arr:
                    arr.append(num)
                else:
                    print("Число уже было введено. Попробуйте снова.")
            else:
                print("Число должно быть от 0 до 100. Попробуйте снова.")
        except ValueError:
            print("Это не число. Попробуйте снова.")

    return arr


if __name__ == "__main__":
    user_array = get_user_input()
    print("Исходный массив:", user_array)
    sorted_array = merge_sort(user_array)
    print("Отсортированный массив:", sorted_array)
