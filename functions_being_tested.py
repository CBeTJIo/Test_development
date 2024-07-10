def uniq_name(*mentors):
    all_list = []
    all_names_list = []
    # print(mentors)
    for m in mentors:
        all_list.extend(m)
    # print(all_list)

    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = ", ".join(sorted(unique_names))

    names = all_names_sorted.split()
    return names


def calc_namecode(name):
    letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
               "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
    name = name.upper()
    code = 0
    for letter in name:
        try:
            ltr_code = letters.index(letter) % 9
        except:
            continue
        if ltr_code == 0:
            ltr_code = 9
        code += ltr_code

    while code > 9:
        curr = code // 10 + code % 10
        code = curr

    return code


def solution(a, b, c):
    D = b ** 2 - 4 * a * c
    if D == 0:
        result = (-b + D ** 0.5) / (2 * a)
        # print(result)
        return result
    elif D < 0:
        # print("корней нет")
        return "корней нет"
    else:
        my_answ = (-b + D ** 0.5) / (2 * a)
        my_answ_1 = (-b - D ** 0.5) / (2 * a)
        # print(my_answ, my_answ_1)
        return [my_answ, my_answ_1]

# solution (1, 4, 3)
# solution (1, 2, 3)