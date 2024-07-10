import pytest

from functions_being_tested import uniq_name, calc_namecode, solution


def test_uniq_name():
    mentors = ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
               "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
               "Азамат Искаков", "Роман Гордиенко", "Филипп Воронов", "Анна Юшина", "Иван Бочаров"]
    result = len(uniq_name(mentors))
    expected = 13
    assert expected == result


def test_uniq_name1():
    mentors = ["Евгений Шмаргунов", "Олег Булыгин", "Александр Ульянцев", "Александр Иванов"]
    result = uniq_name(mentors)
    expected = ["Александр,", "Евгений,", "Олег"]
    assert expected == result


def test_uniq_name2():
    mentors = []
    result = uniq_name(mentors)
    expected = []
    assert expected == result


def test_uniq_name3():
    mentors = ["Евгений Шмаргунов"]
    result = uniq_name(mentors)
    expected = ["Евгений"]
    assert expected == result


def test_calc_name():
    name = "Евгений"
    result = calc_namecode(name)
    expected = 1
    assert expected == result


def test_calc_name1():
    name = "Дмитрий"
    result = calc_namecode(name)
    expected = 7
    assert expected == result


def test_calc_name2():
    name = ""
    result = calc_namecode(name)
    expected = 0
    assert expected == result


@pytest.mark.parametrize(
    'a,b,c,expected',
    (
        [1, 2, 3, 'корней нет'],
        [1, 4, 3, [-1.0, -3.0]]
    )
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert expected == result
