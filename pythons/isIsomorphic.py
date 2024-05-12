class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True
        sdict = {}
        tdict = {}
        
        slst = []
        tlst = []
        
        cur_map = 0
        for cs in s:
            if sdict.get(cs) is None:
                sdict[cs] = cur_map
                cur_map += 1
            slst.append(sdict[cs])
        
        cur_map = 0
        for ct in t:
            if tdict.get(ct) is None:
                tdict[ct] = cur_map
                cur_map += 1
            tlst.append(tdict[ct])
            
        # print(slst)
        # print(tlst)

        for i in range(0, len(s)):
            if tlst[i] != slst[i]:
                return False
        return True
        pass
    
sol = Solution()

s = 'fooooof'
t = 'foooooq'

print(sol.isIsomorphic(s,t))

    