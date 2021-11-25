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

- 45. [把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/) [solution](./offer/_45.py)
- 46. [把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/) [solution](./offer/_46.py)
- 47. [礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/) [solution](./offer/_47.py)
- 48. [最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/) [solution](./offer/_48.py)
