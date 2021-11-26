# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 示例 1:

# 输入：s = "abaccdeff"
# 输出：'b'
# 示例 2:

# 输入：s = ""
# 输出：' '
#

# 限制：

# 0 <= s 的长度 <= 50000


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 此方法需要利用 >=Python3.6 的字典有序(按插入时排序)特性!
        # 用有序集合也是可以的
        recorder = {}
        duplicated = set()

        for char in s:
            if char not in recorder and char not in duplicated:
                recorder[char] = char
            elif char in recorder:
                duplicated.add(recorder.pop(char))

        # 利用 Python3.6 字典排序，这里输出第1个即可!
        for char in recorder:
            return char
        return " "

    # def firstUniqChar(self, s: str) -> str:
    #     counter = Counter(s)
    #     for char in s:
    #         if counter[char] == 1:
    #             return char
    #     return " "


if __name__ == "__main__":
    s = Solution()
    assert s.firstUniqChar("leetcode") == "l"
    assert s.firstUniqChar("abaccdeff") == "b"
    assert s.firstUniqChar("") == " "
    assert s.firstUniqChar("cc") == " "
    assert s.firstUniqChar("ccb") == "b"
    assert s.firstUniqChar("cbdc") == "b"
