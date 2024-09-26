# ID попытки в яндекс контекст - 118897290.

# На самом деле была мысль - отсортировать, но я сразу откинул этот вариант
# т.к. прикинул, что временная сложность сортировки n*logn + проход по массиву
# в худшем случае даст n -> n^2*logn.
# И подумал, что можно быстрее. Замерил время, и, новый алгоритм действительно
# быстрее, чем больше входные данные -> больше разница. И до этого момента
# думал, что временная сложность прошлого алгоритма n^2 при наихудшем раскладе,
# но не учел, что создание словаря Counter похоже также требует линейного
# прохода, получается сложность предыдущего алгоритма n^3?


def platform_couting(robots: list[str], limit: int) -> int:
    '''Считает число минимальное число необходимых платформ.'''
    robots.sort(key=int)
    left_index = 0
    right_index = len(robots) - 1
    platform_amount = 0

    while left_index <= right_index:
        if int(robots[right_index]) + int(robots[left_index]) <= limit:
            left_index += 1
        right_index -= 1
        platform_amount += 1

    return platform_amount


if __name__ == '__main__':
    robots = input().split()
    max_weight = int(input())
    print(platform_couting(robots, max_weight))
