# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 示例 1:

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#

# 提示：

# 0 <= num < 231


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
