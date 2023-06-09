from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    all_jobs = read(path)
    industry = []
    for jobs in all_jobs:
        if jobs["industry"] not in industry and jobs["industry"] != '':
            industry.append(jobs["industry"])
    return industry

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered = []
    for job in jobs:
        if job['industry'] == industry:
            filtered.append(job)
    return filtered
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
