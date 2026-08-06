class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        db = {}
        def dfs(idx):
            # base condition
            if idx == len(s):
                return True

            if idx in db:
                return db[idx]


            for word in wordDict:
                if s.startswith(word, idx):                      
                    if dfs(idx+ len(word)):
                        db[idx] = True
                        return True

            db[idx] = False
            return False                    

        return dfs(0)
        