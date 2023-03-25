from typing import Union, List, Dict
from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    all_jobs = read(path)
    all_salary = []
    for jobs in all_jobs:
        if (
            jobs["max_salary"].isdigit()
            and int(jobs["max_salary"]) not in all_salary
            and jobs["max_salary"] != ""
        ):
            all_salary.append(int(jobs["max_salary"]))
    maximum_salary = max(all_salary)
    return maximum_salary
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    all_jobs = read(path)
    all_salary = []
    for jobs in all_jobs:
        if (
            jobs["min_salary"].isdigit()
            and int(jobs["min_salary"]) not in all_salary
            and jobs["min_salary"] != ""
        ):
            all_salary.append(int(jobs["min_salary"]))
    minimum_salary = min(all_salary)
    return minimum_salary
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if job["min_salary"] <= int(salary) <= job["max_salary"]:
        return True
    return False

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
