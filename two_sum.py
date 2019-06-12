
def two_sum(nums, target):
    result = []
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            result.append(dic[nums[i]])
            result.append(i)
            break
        dic[target - nums[i]] = i
    return result


if __name__ == "__main__":
    nums_ = [2, 7, 11, 15]
    target_ = 9
    result_ = two_sum(nums_, target_)
    print(result_)
