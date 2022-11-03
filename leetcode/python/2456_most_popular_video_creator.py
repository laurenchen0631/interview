class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        mostPopular = dict[str, tuple[str, int]]()
        totalViews = dict[str, int]()
        curMax = 0
        curRes = []
        for i in range(len(creators)):
            creator = creators[i]
            view = views[i]
            title = ids[i]
            totalViews[creator] = totalViews.get(creator, 0) + view
            if curMax < totalViews[creator]:
                curMax = totalViews[creator]
                curRes = [creator]
            elif curMax == totalViews[creator]:
                curRes.append(creator)

            if (creator not in mostPopular) or (mostPopular[creator][1] < view) or (mostPopular[creator][1] == view and mostPopular[creator][0] > title):
                mostPopular[creator] = (title, view)
        return [[creator, mostPopular[creator][0]] for creator in curRes]
    
s = Solution()
print(s.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]))
print(s.mostPopularCreator(creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]))