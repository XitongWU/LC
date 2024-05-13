class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        if strs == [""]:
            return [[""]]
        
        res_lst:list[list[str]] = []
        dict_lst:list[dict] = []
        
        def getDict(s:str) -> dict:
            sdict = {}
            for c in s:
                # print(c)
                if sdict.get(c) is None:
                    sdict[c] = 1
                else:
                    sdict[c] += 1
            return sdict
                    
        # getDict('bat')
        for word in strs:
            dict_len = len(dict_lst)
            word_dict = getDict(word)
            # print(word_dict)
            for i in range(dict_len + 1):
                if i == dict_len:
                    dict_lst.append(word_dict)
                    res_lst.append([word])
                    
                elif word_dict == dict_lst[i]:
                    res_lst[i].append(word)
                    break
        
        return res_lst
    
    
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))
            
            
        