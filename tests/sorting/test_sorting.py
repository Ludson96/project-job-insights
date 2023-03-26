from src.pre_built.sorting import sort_by

job_list = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2022-08-12"},
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2022-04-27"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-10-17"},
]

jobs_list_max = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2022-08-12"},
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2022-04-27"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-10-17"},
]

jobs_list_date = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-10-17"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2022-08-12"},
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2022-04-27"},
]

job_list_min = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-10-17"},
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2022-04-27"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2022-08-12"},
]


def test_sort_by_criteria():
    sort_by(job_list, "max_salary")
    assert job_list == jobs_list_max
    sort_by(job_list, "date_posted")
    assert job_list == jobs_list_date
    sort_by(job_list, "min_salary")
    assert job_list == job_list_min
