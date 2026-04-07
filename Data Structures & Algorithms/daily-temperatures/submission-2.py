class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # кладем первый - если больше - расстояние, если меньше или равно - кладем 
        # если больше, то расстояние до верхнего, удаляем, расстояние до след - удаляем
        # кладем тот, что сравнивали
        # ввод: 30 29 31 32 вывод: 1 2 1 0, а должен быть: 2 1 1 0
        # 31 - 3
        # 29 - 2
        # 30 - 1

        ans = ['0'] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                ans[stack[-1]] = i  - stack[-1]
                stack.pop()
            else:
                stack.append(i) # i - temperatures.index(i) - в моих мыслях
        return ans