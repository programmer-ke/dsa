"""A Naive Suffix Array Implementation"""


class SuffixArray:
    def __init__(self, haystack: str):
        self._array = sorted([haystack[i:] for i in range(0, len(haystack))])

    def _find(self, needle):
        """Return the index of needle or -1"""
        start, end = 0, len(self._array)
        while start < end:
            mid = (start + end) // 2
            mid_value = self._array[mid]
            if mid_value.startswith(needle):
                return mid
            elif mid_value > needle:
                end = mid
            else:
                start = mid + 1
        return -1

    def _find_start_index(self, prefix):
        """Returns the starting index of prefix if exists"""
        index = self._find(prefix)
        while index - 1 >= 0 and self._array[index - 1].startswith(prefix):
            index -= 1
        return index

    def find_shortest(self, prefix: str) -> str | None:
        """Shortest substring that has this beginning"""
        index = self._find_start_index(prefix)
        if index < 0:
            return None
        length, shortest = len(self._array[index]), self._array[index]
        while index + 1 < len(self._array) and self._array[index + 1].startswith(
            prefix
        ):
            index += 1
            if len(self._array[index]) < length:
                length, shortest = len(self._array[index]), self._array[index]
        return shortest

    def find_longest(self, prefix: str) -> str | None:
        """Longest substring that has this beginning"""
        index = self._find_start_index(prefix)
        if index < 0:
            return None
        length, longest = len(self._array[index]), self._array[index]
        while index + 1 < len(self._array) and self._array[index + 1].startswith(
            prefix
        ):
            index += 1
            if len(self._array[index]) > length:
                length, longest = len(self._array[index]), self._array[index]
        return longest

    def find_all(self, prefix: str) -> list[str]:
        """All substrings that have this beginning"""
        index = self._find_start_index(prefix)
        matching = []
        while 0 <= index < len(self._array) and self._array[index].startswith(prefix):
            matching.append(self._array[index])
            index += 1
        return matching
