# ID попытки в яндекс контекст - 118897290.

def platform_couting(robots: list[int], limit: int) -> int:
    '''Считает число минимальное число необходимых платформ.'''
    sorted_robots = sorted(robots)
    the_lightest_robot: int = 0
    the_heaviest_robot: int = len(sorted_robots) - 1
    platform_amount: int = 0

    while the_lightest_robot <= the_heaviest_robot:
        if (int(sorted_robots[the_heaviest_robot]) +
                int(sorted_robots[the_lightest_robot]) <= limit):
            the_lightest_robot += 1
        the_heaviest_robot -= 1
        platform_amount += 1

    return platform_amount


if __name__ == '__main__':
    robots = [int(weight) for weight in input().split()]
    platform_limit = int(input())
    print(platform_couting(robots, platform_limit))
