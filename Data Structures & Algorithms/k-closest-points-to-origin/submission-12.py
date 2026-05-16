class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: (x[0] * x[0]) + (x[1] * x[1])

        def quickSelect(l, r):
            print(l, r)
            pivot = euclidean(points[r])
            print(euclidean(points[l]), euclidean(points[r]), pivot)
            p = r

            j = l
            for i in range(l, r):
                if euclidean(points[i]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    j += 1
            print(p, j)
            points[j], points[p] = points[p], points[j]
            return j
            

                

        P = len(points)
        l, r = 0, len(points) - 1
        while P != k:
            P = quickSelect(l, r)
            print(points)

            if P < k:
                l = P + 1
            else:
                r = P - 1
        return points[:P]
            


