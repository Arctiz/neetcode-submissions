class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = set()
        group = []

        for string in strs:
            string = sorted(string)
            sort.add("".join(string))

        for i in sort:
            temp = []
            for string in strs:
                if "".join(sorted(string)) == i:
                    temp.append(string)
            group.append(temp)
        return group
