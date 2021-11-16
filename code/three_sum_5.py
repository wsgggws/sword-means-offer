def three_sum_force(nums: list) -> list:
    # 暴力 => O(n*n*n)
    nums.sort()
    length = len(nums)
    result = []
    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
    return result


def three_sum_map(nums: list) -> list:
    # 使用 map 优化第三层 for => O(n*n)
    nums.sort()
    maps = {-value: index for index, value in enumerate(nums)}
    length = len(nums)
    result = []
    for i in range(0, length):
        for j in range(i + 1, length):
            value = nums[i] + nums[j]
            if value in maps and maps[value] > j and [nums[i], nums[j], nums[maps[value]]] not in result:
                result.append([nums[i], nums[j], nums[maps[value]]])
    return result


def three_sum_double_point(nums: list) -> list:
    # TODO 使用双指针
    ...


if __name__ == "__main__":
    assert three_sum_force([-1, 2, 1, 0]) == [[-1, 0, 1]]
    assert three_sum_force([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum_map([-1, 2, 1, 0]) == [[-1, 0, 1]]
    assert three_sum_map([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
