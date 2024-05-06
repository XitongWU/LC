class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or len(s) >= 201:
            return 0
        positive = 1
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] != " ":
                if s[i] == '-' or s[i] == "+":
                    for j in range(i):
                        if s[j] == "0":
                            return 0
                    break
                elif s[i].isdigit():
                    if int(s[i]) > 0:
                        break
                else:
                    return 0

        for i in range(len(s)):
            if s[i] == "+":
                positive = 1
                if i+1>=len(s):
                    return 0
                if not s[i+1].isdigit():
                    return 0
            if s[i] == "-":
                positive = -1
                if i + 1 >= len(s):
                    return 0
                if not s[i + 1].isdigit():
                    return 0
            if s[i].isdigit():
                if int(s[i]) > 0:
                    start = i
                    break
                    # return start

        if start == len(s) - 1:
            end = start + 1
        else:
            for i in range(start, len(s)):
                if not s[i].isdigit():
                    end = i
                    break
                end = len(s)
        sr = s[start:end]

        res = 0
        if s[start] == ' ':
            return 0
        for i in range(len(sr) - 1, -1, -1):
            res += int(sr[i]) * 10 ** (len(sr) - 1 - i)
            #pass
        # print(sr)
        # print(positive*res)
        print(start)
        print(end)
        res = res * positive
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31


def main():
    s = input()
    # s = '            -434.a232 aa  '

    s1 = Solution()
    print(s1.myAtoi(s))


if __name__ == "__main__":
    main()
