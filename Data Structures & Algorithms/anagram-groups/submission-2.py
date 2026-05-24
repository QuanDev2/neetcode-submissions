class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # go through strs (n length)
        # # each str, sorted
        # s_strs = []
        # for str in strs:
        #     s_strs.append("".join(sorted(str))) # O(mlog(m)) time and O(m) space; m being length of the longest str
            

        # # temp result: hashmap of lists; convert later
        # result = {}
        # for i, s_str in enumerate(s_strs): # ['act', 'opst', 'opst', 'act', 'opst', 'aht']
        #     if s_str in result:
        #         result[s_str].append(i)
        #     else:
        #         result[s_str] = [i]
        
        # result_list = []
        # for s_str, idx_list in result.items():
        #     anagrams = []
        #     for i in idx_list: # [0, 2, 3]
        #         anagrams.append(strs[i])
        #     result_list.append(anagrams)

        # return result_list

        ## Short solution, defaultdict, append in place
        res = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            res[sortedStr].append(s)
        
        return list(res.values())
        
        
        
        
        