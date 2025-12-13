class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices
        max_area = 0
        
        # Add a 0 height at the end to flush the stack
        heights.append(0)
        
        for i, h in enumerate(heights):
            # Pop while current bar is shorter than the stack top
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                
                # If stack empty, width = i (from index 0 to i-1)
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                    
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area