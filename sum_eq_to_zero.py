class sum_to_zero:
    def cal(self, nums):
        tot_prod = 1
        for i in nums:
            if i != 0:
              tot_prod *= i
            
        output = []
        for i in nums:
            if i != 0:
                output.append(tot_prod // i)
            else:
                if nums.count(0) > 1:
                    output.append(0)
                else:
                    output.append(tot_prod)
        return output
    
if __name__ == "__main__":
    obj = sum_to_zero()
    nums = input("enter num = ")
    nums = list(map(int, nums.split()))
    res = obj.cal(nums)
    print(res)
