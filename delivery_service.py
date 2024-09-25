# ID попытки в яндекс контекст - 118841418.
# P.S. Я пытался найти более оптимальное решение, но ничего не приходило
# в голову, поэтому корявенько и скорее всего далеко не оптимально, но сделал.
# С нетерпением жду замечаний и советов ;)
from collections import Counter


def platform_couting(robots: list, limit: int):
    '''Считает число минимальное число необходимых платформ.'''
    robots_dict: dict = Counter(robots)
    platforms_amount: int = 0

    for robot_mass in robots_dict:
        # Запускаем цикл до тех пор, пока количество роботов данной массы
        # не обработается.
        while robots_dict[robot_mass]:
            # Обработка робота равного по массе лимиту.
            if int(robot_mass) == limit:
                platforms_amount += robots_dict[robot_mass]
                robots_dict[robot_mass] = 0
                continue

            # Обработка возможной пары робота, дающая в сумму лимит.
            elif (robots_dict.get(pair := str(limit - int(robot_mass)))
                  and check_same_robot(pair, robot_mass, robots_dict)):
                result = processing_pair(robot_mass, pair, robots_dict)
                if result:
                    platforms_amount += result
                    continue

            # Перебор доступных пар для данного робота.
            available_pairs = [
                num for num in robots_dict
                if robots_dict[num] and int(num) + int(robot_mass) < limit
                and check_same_robot(num, robot_mass, robots_dict)]

            if available_pairs:
                # Рассматриваем вариант дающий максимальный по сумме результат
                # для создания оптимального количества пар.
                result = processing_pair(robot_mass, max(available_pairs),
                                         robots_dict)
                platforms_amount += result
                continue

            else:
                robots_dict[robot_mass] -= 1
                platforms_amount += 1

    return platforms_amount


def processing_pair(first_mass: str, second_mass: str, all_mass: dict) -> int:
    '''
    Обрабатывавет переданную пару роботов и возвращает количество платформ.
    '''
    if second_mass == first_mass:
        platforms = all_mass[first_mass] // 2
    else:
        platforms = min(
            all_mass[second_mass],
            all_mass[first_mass])
    all_mass[first_mass] -= platforms
    all_mass[second_mass] -= platforms
    return platforms


def check_same_robot(first_mass: str,
                     second_mass: str, all_mass: dict) -> bool:
    '''
    Функция - предикант.
    Проверяет наличие нескольких роботов одной массы.
    Исключает обработку одного и того же робота -> ошибки.
    '''
    return not (first_mass == second_mass and all_mass[first_mass] == 1)


if __name__ == '__main__':
    robots = input().split()
    max_weigth = int(input())
    print(platform_couting(robots, max_weigth))
