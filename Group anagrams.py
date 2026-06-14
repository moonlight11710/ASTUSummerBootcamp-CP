class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keep = {}
        ans = []
        for i in strs:
            word = "".join(sorted(i))
            if word in keep:
                keep[word].append(i)
            else:
                keep[word]=[i]
        for i in keep:
            ans.append(keep[i])
        return ans
