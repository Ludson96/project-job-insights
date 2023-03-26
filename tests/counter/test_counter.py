from src.pre_built.counter import count_ocurrences


def test_counter():
    count_python = count_ocurrences("data/jobs.csv", "Python")
    assert count_python == 1639
