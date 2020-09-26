
class Solution:
    def maxArea(self, height: list) -> int:
        answer = -1

        # print('height',height)

        left = 0
        right = len(height)-1
        max_area = 0
        while left != right:
            # print('left',left,'right',right,'max_area',max_area)
            new_area = min(height[left],height[right]) * (right - left)
            if new_area > max_area:
                max_area = new_area
                # print('max_area',max_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        answer = max_area

        return answer









print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))