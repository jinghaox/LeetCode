class solution(object):
    def twoSum(self, s, target):
        s = sorted(s)
        i = 0
        j = len(s)-1
        ret = []
        while i < j:
            if s[i] + s[j] < target:
                i += 1
            elif s[i] + s[j] > target:
                j -= 1
            else:
                ret.append([s[i], s[j]])
                break

        return ret

    def threeSum(self, s, target):
        s = sorted(s)
        ret = []
        for low in range(len(s)-2):
            i = low+1
            j = len(s)-1
            while i<j:
                if s[low]+s[i]+s[j] < target:
                    i += 1
                elif s[low]+s[i]+s[j] > target:
                    j -= 1
                else:
                    ret.append([s[low], s[i], s[j]])
                    break
        return ret

    def fourSum(self, s, target):
        """
        x x x x x x x x x
        begin:
        f s i...........j

        end  
                  f s i j
        
        also need to handle repeatitions
        """
        s.sort()
        # s = sorted(s) is slow
        ret = []
        for first in range(len(s)-3):
            # need to take care of repeatitions
            if first > 0 and s[first] == s[first-1]:
                # not first += 1, but continue
                # means the current loop will be skiped
                continue
            for second in range(first+1, len(s)-2):
                if second > first+1 and s[second] == s[second-1]:
                    continue
                i = second+1
                j = len(s)-1
                while i < j:
                    if s[first] + s[second] + s[i] + s[j] < target:
                        i += 1
                    elif s[first] + s[second] + s[i] + s[j] > target:
                        j -= 1
                    else:
                        ret.append([s[first], s[second], s[i], s[j]])
                        # here shouldn't break, but continue
                        while i < j and s[i] == s[i+1]:
                            i += 1
                        while i < j and s[j] == s[j-1]:
                            j -= 1
                        i += 1
                        j -= 1

        return ret

    def fourSumHash(self, nums, target):
        _len, _dict, ret = len(nums), {}, [] 
        if _len < 4:
            return []
        # sort the nums, so we can avoid permutations, such as [-5, 0 , 2, 3] and [-5, 2, 0 ,3]
        nums.sort()
        for i in range(_len):
            for j in range(i+1, _len):
                _sum = nums[i] + nums[j]
                if _sum not in _dict:
                    _dict[_sum] = [[i,j]]
                else:
                    # here we may have repeatitions
                    # e.g. [-2,-1,0,0,1,2,3]
                    # two 0s, but their index [i,j] are different
                    _dict[_sum].append([i,j])
        
        for i in range(_len):
            for j in range(i+1, _len):
                _diff = target - (nums[i] + nums[j])
                if _diff in _dict:
                    for k in _dict[_diff]:
                        if k[0] > j:
                            ret.append([nums[i], nums[j], nums[k[0]], nums[k[1]]])
        # remove duplicates
        ret.sort()
        res = [ret[i] for i in range(len(ret)) if i==0 or ret[i] != ret[i-1]]
        return res

    def fourSumSet(self, nums, target):
        """
        This one returns list of tuples, not list of lists
        But seems that LeetCode accepted this
        """
        _len,_dict,ans = len(nums),{},set()
        nums.sort()
        if len(nums) < 4 or 4*nums[0] > target or 4*nums[_len-1] < target:
        	return []
        for i in range(_len):
        	for j in range(i + 1,_len):
        		_sum = nums[i] + nums[j]
        		if _sum not in _dict:
        			_dict[_sum] = [(i,j)]
        		else:
        			_dict[_sum].append((i,j))
        for i in range(_len):
        	for j in range(i + 1,_len):
        		_cha = target - (nums[i] + nums[j])
        		if _cha in _dict:
        			for k in _dict[_cha]:
        				if k[0] > j:
        					ans.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return list(ans)

sol = solution()
s = [1, 0, -1, 0, -2, 2, 1, 3]
ret = sol.twoSum(s, 5)
print(ret)
ret = sol.threeSum(s, 0)
print(ret)
ret = sol.fourSum(s, 0)
print(ret)
ret = sol.fourSumSet(s, 0)
print(ret)
