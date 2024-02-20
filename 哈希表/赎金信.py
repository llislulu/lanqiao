class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_a = dict()
        for i in magazine:
            hash_a[i] = hash_a.get(i, 0) + 1
        for j in ransomNote:
            if j not in hash_a or hash_a[j] == 0:
                return False
            hash_a[j] -=1
        return True

