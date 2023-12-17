import heapq


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_heap = {}
        self.rating = {}
        self.food_to_cuisine = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []
            self.cuisine_heap[cuisine].append((-rating, food))
            self.rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            
        for cuisine in self.cuisine_heap:
            heapq.heapify(self.cuisine_heap[cuisine])
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.rating[food] = newRating
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_heap[cuisine]:
            rating, food = self.cuisine_heap[cuisine][0]
            if rating == -self.rating[food]:
                return food
            else:
                heapq.heappop(self.cuisine_heap[cuisine])
        return ''
        
