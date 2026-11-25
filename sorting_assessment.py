def extract_unique_letters(full_name: str) -> list[str]:
    """Extracts unique alphabetic letters in order, excluding symbols and spaces."""
    seen = set()
    result = []
    for char in full_name.upper():
        if char.isalpha() and char not in seen:
            seen.add(char)
            result.append(char)
    return result


def merge_sort(arr: list[str]) -> list[str]:
    """Sorts a list of characters alphabetically using Merge Sort (Divide and Conquer)."""
    if len(arr) <= 1:
        return arr

    # 1. Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 2. Conquer & Combine
    return merge(left_half, right_half)


def merge(left: list[str], right: list[str]) -> list[str]:
    """Merges two sorted lists into a single alphabetically sorted list."""
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def main() -> None:
    full_name = "Edmer Jehoash D. Orendain"
    unsorted_array = extract_unique_letters(full_name)
    sorted_array = merge_sort(unsorted_array)

    print("Full Name:     ", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)


if __name__ == "__main__":
    main()