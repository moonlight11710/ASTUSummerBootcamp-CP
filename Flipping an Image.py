class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i = i.reverse()
        image = [[0 if j==1 else 1 for j in i]for i in image]
        return image
