from typing import Set, List

def split(array: List[str], group_count : int = 0) -> Set[List[List[str]]]:
    """
    Calculates the possible splittings of the array.

    Splitting Rules:
     - Array is splitted into N (group_count) parts.
     - Each parts is at least 2 element long.
     - First and Last element of each part is the same.

     Example:
         split([ a, a, b, b ], 2) = { [ [a, a], [b,b] }
         split([ a, a, b, a, b ], 2) = { [ [a, a], [b, a, b] }
         split([ a, a, b, b ], 3) = { }

    Notes:
        - Use List indexes for splitting array
        ```
        head, tail = list[:3], list[3:]
        ```
    """
    return {}