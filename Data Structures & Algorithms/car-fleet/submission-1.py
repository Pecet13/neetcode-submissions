class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True, key=lambda item: item[0])
        fleets = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)
        