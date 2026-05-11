class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        print(cars)

        stack = []


        for (p, s) in cars:
            cur = (target - p) / s
            if stack and stack[-1] >= cur:
                continue
            else:
                stack.append(cur)
        print(stack)
        return len(stack)