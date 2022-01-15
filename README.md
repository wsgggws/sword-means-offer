# DayDayUp


### 设计

##### 1. 有一个随机生成器，只能生成0，1，但概率不公平，那么如何设计得到一个公平的方案？

##### 2. 比如一个错误日志，2021_10_27.log，我需要统计"error"这个单词出现的日志条数，该用什么命令？ 根据2021_10_27.log，如何计算error出现的峰值（以小时为单位，峰值可能存在多个，统计每一次峰值）

##### 3. 简述 Regex 的实现原理？想些办法降低它的 灾难性回溯？ 在 Python 中先使用 re.compile 成 pattern 有优势吗？有哪些优势？

##### 4. 如果要开发一个「热点评论」的功能，请先大致说说你的设计架构

##### 5. 如何让 Hash 表有序

##### 6. 如何对接口进行限流？

##### 7. 谈谈你对REST和RPC的看法

##### 8. 如何写出烂代码

### 数学

##### 1. 有50个人，那么有两个人生日是同一天的概率是多少？ [solution](./math/1_probability.md)

##### 2. 一天内(24小时)，分针和时针会重合几次? [solution](./math/2_duplicate.md)

##### 3. 哥哥，弟弟，妹妹三人想到达直线距离为 28km 外的大树，有一辆车速可达 60km/h 的摩托车，但包括驾驶人在内只限坐 2 人, 3 人的步行均为 15km/h, 问他们到达大树的最短时间是多久？ [solution](./math/3_short_time.md)


### 编程
##### 1. 给定（[{)]} 这样的字符串， 验证是否为括号字符串： 如()({})这种 [solution](./code/parentheses_1.py)

##### 2. 如何把一个字符串 转化为一个小数(string 转 double） [solution](./code/char2num_2.py)

##### 3. 将小写金额转换成大写。不考虑负数，精确到亿，小数点后超过两位部分四舍五入. 示例： [solution](./code/num2zhcn_3.py)
```
输入：10234.567
输出：壹万零贰佰叁拾肆元伍角柒分
输入：123045607.12
输出：壹亿贰仟叁佰零肆万伍仟陆佰零柒元壹角贰分
输入：98
输出：玖拾捌元整
输入：98.00
输出：玖拾捌元整
```

##### 4. 给你一个字符串，输出频率最高且最先出现的字符 [solution](./code/find_max_occur_char_4.py)
```
Input: Hello world, every one!
Output: e
```

##### 5. 三数之和 [solution](./code/three_sum_5.py)

### 剑指 Offer

- [04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)     [solution](./offer/_04.py)      [video](https://www.bilibili.com/video/BV1Vi4y1o7vx/)
- [06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)     [solution](./offer/_06.py)      [video](https://www.bilibili.com/video/BV1gZ4y1X7MZ/)
- [10-I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)     [solution](./offer/_10_i.py)      [video](https://www.bilibili.com/video/BV1pY411H7d4/)
- [10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)     [solution](./offer/_10_ii.py)      [video](https://www.bilibili.com/video/BV1mR4y1W7G8/)
- [11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)     [solution](./offer/_11.py)      [video](https://www.bilibili.com/video/BV1A44y177oj/)
- [12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)     [solution](./offer/_12.py)      [video](https://www.bilibili.com/video/BV1PQ4y1Y7RB/)
- [15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)     [solution](./offer/_15.py)      [video](https://www.bilibili.com/video/BV1Um4y1X7Tb/)
- [16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)     [solution](./offer/_16.py)      [video](https://www.bilibili.com/video/BV1fq4y1w7tB/)
- [17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)     [solution](./offer/_17.py)      [video](https://www.bilibili.com/video/BV1za411q7v4/)
- [18. 删除链表的节点-递归实现](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)     [solution](./offer/_18_i.py)      [video](https://www.bilibili.com/video/BV1iY411H7Yc/)
- [18. 删除链表的节点-非递归实现](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)     [solution](./offer/_18_ii.py)      [video](https://www.bilibili.com/video/BV13F411B7c2/)
- [20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)     [solution](./offer/_20.py)      [video](https://www.bilibili.com/video/BV1ku41127L6/)
- [21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)     [solution](./offer/_21.py)      [video](https://www.bilibili.com/video/BV1fi4y197NQ/)
- [24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)     [solution](./offer/_24.py)      [video](https://www.bilibili.com/video/BV1b44y1J72N/)
- [31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)     [solution](./offer/_31.py)      [video](https://www.bilibili.com/video/BV1Ki4y1o7VZ/)
- [38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)     [solution](./offer/_38.py)      [video](https://www.bilibili.com/video/BV1QZ4y1S75m/)
- [39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)     [solution](./offer/_39.py)      [video](https://www.bilibili.com/video/BV1bT4y1m7Pa/)
- [42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)     [solution](./offer/_42.py)      [video](https://www.bilibili.com/video/BV1M44y1L73E/)
- [44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)     [solution](./offer/_44.py)      [video](https://www.bilibili.com/video/BV1RU4y1T7Jp)
- [45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)      [solution](./offer/_45.py)       [video](https://www.bilibili.com/video/BV18b4y1b7YB/)
- [46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)       [solution](./offer/_46.py)      [video](https://www.bilibili.com/video/BV14M4y1P7kv/)
- [47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)      [solution](./offer/_47.py)   [video](https://www.bilibili.com/video/BV1uU4y1T7Aj/)
- [48. 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)    [solution](./offer/_48.py)      [video](https://www.bilibili.com/video/BV1j3411b7sg/)
- [49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)       [solution](./code/_49.py)       [video](https://www.bilibili.com/video/BV1Wf4y1K7vr/)
- [50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)     [solution](./offer/_50.py)      [video](https://www.bilibili.com/video/BV1iq4y1B7PM/)
- [58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)     [solution](./offer/_58.py)      [video](https://www.bilibili.com/video/BV1hL4y1b72y/)
- [63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)     [solution](./offer/_63.py)      [video](https://www.bilibili.com/video/BV1YU4y1K7yA/)
- [66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)     [solution](./offer/_66.py)      [video](https://www.bilibili.com/video/BV1hF411z74E/)
- [67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)      [solution](./offer/_67.py)      [video](https://www.bilibili.com/video/BV1wQ4y1v7GW/)
- [II 005. 单词长度的最大乘积](https://leetcode-cn.com/problems/aseY1I/)      [solution](./offer/ii_005.py)       [video](https://www.bilibili.com/video/BV1N3411t7RT/)
- [II 008. 和大于等于 target 的最短子数组](https://leetcode-cn.com/problems/2VG8Kg/)      [solution](./offer/ii_008.py)       [video](https://www.bilibili.com/video/BV15P4y1G7SQ/)
