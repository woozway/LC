class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totdis = 0
        summation = [0]*len(distance)
        for i, x in enumerate(distance):
            totdis += x
            if i != 0:
                summation[i] = summation[i-1] + distance[i-1]
        a, b = sorted([start, destination])
        diff = summation[b] - summation[a]
        return min(diff, totdis-diff)
