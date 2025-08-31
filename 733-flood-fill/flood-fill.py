class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        colms = len(image[0])
        c_color = image[sr][sc]
        def dfs(sr,sc):
            if (sr < 0 or sc < 0 or sr >= rows or sc >= colms or image[sr][sc]!=c_color):
                return
            if c_color == color:
                return
            image[sr][sc] = color
            dfs(sr+1,sc)
            dfs(sr,sc+1)
            dfs(sr-1,sc)
            dfs(sr,sc-1)
        dfs(sr,sc)
        return image
        

