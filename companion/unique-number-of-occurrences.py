class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = Counter(arr)
        return len(occurrence) == len(set(occurrence.values()))