def binary_search(array, target):
    """
    Implementiert die Binäre Suche.

    :param array: Sortierte Liste, in der gesucht wird.
    :param target: Das zu suchende Element.
    :return: Index des Elements oder -1, wenn es nicht gefunden wird.
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1