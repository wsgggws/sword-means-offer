class Solution:
    def translateNum(self, num: int) -> int:
        text = "0" + str(num)
        dp = []
        # dp[n] 表示前 n 个字符所能实现的翻译方法
        # 则 dp[n] = dp[n-1]，当最后两位不能用 j-z 表示，即最后一位只能依附在 dp[n-1] 种的最后面
        #          = dp[n-1] + dp[n-2], 当最后两位能使用 j-z 表示，则可有最后两位依附在 dp[n-2] 种的后面 + 最后一位依附在 dp[n-1] 种的后面
        dp[0], dp[1] = 1, 1
        for i in range(2, len(text)):
            if 10 <= int(text[i - 1 : i + 1]) <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(text) - 1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.translateNum(12258) == 5
    assert solution.translateNum(1) == 1
    assert solution.translateNum(12) == 2
    assert solution.translateNum(102) == 2
