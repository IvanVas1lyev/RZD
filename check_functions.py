from constants import *
import pandas as pd


def check_rotate_shipments_order(permutation: list, params_list: list) -> list:
    """
    rotate shipments to optimal state and call check function
    :param permutation: permutation of shipments
    :param params_list: list of shuffled shipments parameters
    :return: result of check() function call
    """
    final_order = []

    # вращение каждого груза в горизонтальной плоскости для оптимального размещения
    for params in params_list:
        max_measurement = max(params[0], params[1])
        min_measurement = max(params[0], params[1])

        if max_measurement - W > DELTA:
            if min_measurement - W > DELTA:
                return final_order

            params[0] = max_measurement
            params[1] = min_measurement
        else:
            params[0] = min_measurement
            params[1] = max_measurement

    return check_shipments_order(permutation, params_list)


def check_all_forces(start: float, end: float, arr_for_check: list) -> bool | list:
    """
    calculates and tests forces
    :param start: start of series of shipments
    :param end: end of series of shipments
    :param arr_for_check: list of ordered shipments params
    :return: flag
    """
    length = len(arr_for_check)
    flag = True

    data_dict = {
        '№ п/п': range(1, length + 1),
        '№ Груза': range(1, length + 1),
        'Длина': [arr_for_check[i][0] for i in range(length)],
        'Ширина': [arr_for_check[i][1] for i in range(length)],
        'Высота': [arr_for_check[i][2] for i in range(length)],
        'Кол-во (штук)': [arr_for_check[i][3] for i in range(length)],
        'Вес 1 ед. (кг)': [arr_for_check[i][4] for i in range(length)]
    }

    rzhd_df = pd.DataFrame(data_dict)
    my_list = []

    for i in range(length):
        if i == 0:
            my_list.append(start + rzhd_df['Длина'][i] / 2)
        else:
            my_list.append(start + rzhd_df['Длина'][i] / 2 + rzhd_df['Длина'].cumsum().iloc[i - 1])

    rzhd_df['ДлинаЦТ'] = my_list
    my_list = []

    for i in range(length):
        my_list.append(abs(rzhd_df['ДлинаЦТ'][i] - L / 2))

    rzhd_df['РастЦТ'] = my_list

    # Продольное смещение грузов в вагоне:
    l1 = 0.5 * L - sum(rzhd_df['ДлинаЦТ'] * rzhd_df['Вес 1 ед. (кг)'] / 1000) / sum(rzhd_df['Вес 1 ед. (кг)'] / 1000)
    l1 = round(l1, 2)

    # Продольное смещение грузов с вагоном:
    l2 = 0.5 * L - (sum(rzhd_df['ДлинаЦТ'] * rzhd_df['Вес 1 ед. (кг)'] / 1000) + Q * Lv) / (
            sum(rzhd_df['Вес 1 ед. (кг)'] / 1000) + Q)
    l2 = round(l2, 2)

    # Высота ЦТ грузов в вагоне:
    h1 = sum((rzhd_df['Высота'] / 2 + Hugr) * rzhd_df['Вес 1 ед. (кг)'] / 1000) / sum(rzhd_df['Вес 1 ед. (кг)'] / 1000)
    h1 = round(h1, 2)

    # Общая высота ЦТ
    h2 = (sum((rzhd_df['Высота'] / 2 + Hugr) * rzhd_df['Вес 1 ед. (кг)'] / 1000) + Q * Hv) / (
                sum(rzhd_df['Вес 1 ед. (кг)'] / 1000) + Q)
    h2 = round(h2, 2)
    # Расчет наветренной поверхности
    s = Svag + sum(rzhd_df['Высота'] / 1000 + rzhd_df['Длина'] / 1000)
    s = round(s, 2)

    if h2 >= 2300:
        flag = False
    if s >= 50:
        flag = False

    # Силы действующие на i-й груз
    my_arr = []

    for i in range(length):
        # 1 Продольная инерционная сила
        Apr = a22 - (sum(rzhd_df['Вес 1 ед. (кг)'] / 1000)) * (a22 - a94) / 72
        Fpr = Apr * rzhd_df['Вес 1 ед. (кг)'][i] / 1000

        # 2 Поперечная инерционная сила
        Ap = 0.33 + 0.44 / LL * rzhd_df['РастЦТ'][i]
        Fp = Ap * rzhd_df['Вес 1 ед. (кг)'][i] / 1000

        # 3 Вертикальная инерционная сила
        Av = 0.25 + 5e-6 * rzhd_df['Длина'][i] + 2.14 / sum(rzhd_df['Вес 1 ед. (кг)'] / 1000)
        Fv = Av * rzhd_df['Вес 1 ед. (кг)'][i] / 1000

        # 4 Ветровая нагрузка
        Wv = 50 * (rzhd_df['Высота'][i] / 1000 + rzhd_df['Длина'][i] / 1000) / 1000

        # 5 Сила трения в продольном направлении
        Ftrpr = mu * rzhd_df['Вес 1 ед. (кг)'][i] / 1000

        # 6 Сила трения в поперечном направлении
        Ftrp = mu * rzhd_df['Вес 1 ед. (кг)'][i] / 1000 * (1 - Av)

        # 7 Усилия которые должны восприниматься средствами крепления (продольные и поперечные)
        delta_Fpr = Fpr - Ftrpr
        delta_Fp = 1.25 * (Fp + Wv) - Ftrp

        # 8 Коэффициент запаса устойчивости от опрокидывания вдоль вагона
        Npr = rzhd_df['Длина'][i] / 2 / (rzhd_df['Высота'][i] / 2 - Hpry) / Apr

        # 9 Коэффициент запаса устойчивости от опрокидывания поперек вагона
        Np = (rzhd_df['Вес 1 ед. (кг)'][i] / 1000 * min(rzhd_df['Ширина'][i] / 2, 1435)) / (
                    Fp * (rzhd_df['Высота'][i] / 2 - Hpy) + Wv * (rzhd_df['Высота'][i] / 2 - Hpy))

        if (Npr <= 1.25) or (Np <= 1.25):
            flag = False

        my_arr.append([round(Fpr, 2), round(Fp, 2), round(Fv, 2), round(Wv, 2), round(Ftrpr, 2), round(Ftrp, 2),
                       round(delta_Fpr, 2), round(delta_Fp, 2), round(Npr, 2), round(Np, 2)])
    if not flag:
        return False

    return [l1, l2, h1, h2, s, my_arr]


def check_shipments_order(permutation: list, params_list: list) -> list:
    """
    checks the possibility of placing shipments
    :param permutation: permutation of shipments
    :param params_list: list of shuffled shipments parameters
    :return: list of ordered shipments params
    """
    summary_len = 0
    arr_for_check = []
    final_arr_with_coordinates = []

    for index in permutation:
        summary_len += params_list[index - 1][0]
        arr_for_check += [params_list[index - 1]]

    summary_len += (len(permutation) - 1) * MIN_DIST

    if summary_len > L:
        return []

    start = (L - summary_len) / 2
    end = L - (L - summary_len) / 2

    flag = check_all_forces(start, end, arr_for_check)

    if not flag:
        return []

    for elem in arr_for_check:
        new_elem = [start, start + elem[0], elem[1], elem[2]]
        start += elem[0] + MIN_DIST
        final_arr_with_coordinates.append(new_elem)

    return [final_arr_with_coordinates, flag]
