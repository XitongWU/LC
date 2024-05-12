class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) ==0 or len(s)>=401:
            return 0
        start = 0
        end = 0
        positive = 1
        res = 0
        for i in range(len(s)):
            if s[i] != " ":
                if s[i] == "+" or s[i] == '-' or s[i].isdigit():
                    start = i
                    break
                else:
                    return 0
        if s[start] == ' ':
            return 0

        if start == len(s)-1:
            end = start + 1
        else:
            for i in range(start + 1, len(s)):
                if not s[i].isdigit():
                    end = i
                    break
                if i == len(s) - 1:
                    end = len(s)
        # print(start)
        # print(end)
        s = s[start:end]
        if s[0] == "-":
            positive = -1
            s = s[1:]
        elif s[0] == "+":
            positive = 1
            s = s[1:]
        for i in range(len(s) - 1, -1, -1):
            res += int(s[i]) * 10 ** (len(s) - 1 - i)
        res = positive*res
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31


s = input()
sol = Solution()
print(sol.myAtoi(s))