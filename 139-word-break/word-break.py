class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        db = {}
        def dfs(idx):
            # base condition
            if idx == len(s):
                return True

            if idx in db:
                #print(f"db in base condition : {db}")
                return db[idx]


            for word in wordDict:
                if s.startswith(word, idx):                      
                    if dfs(idx + len(word)):
                        #db[idx] = True
                        #print(f"db when match is successful : {db}")
                        return True

            db[idx] = False
            #print(f"db when match is not successful : {db}")
            return False                    

        return dfs(0)
        