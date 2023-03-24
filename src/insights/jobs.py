import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        result = [row for row in reader]
        return result
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    all_jobs = read(path)
    job_types = []
    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered.append(job)
    return filtered
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
