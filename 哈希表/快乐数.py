
class Solution:
    def get_n(self ,n: int):
        new_n = 0
        while n:

            n,r = divmod(n, 10)
            new_n += r * r
        return new_n
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            n = self.get_n(n)
            print(record)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)
solution = Solution()
print(solution.isHappy(2**31 -3))