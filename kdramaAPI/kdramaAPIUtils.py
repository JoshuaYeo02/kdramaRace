# FROM https://github.com/TheBoringDude/kuryana
from typing import Dict, Any, Tuple

from kdramaAPISearch import Search
from kdramaAPIFetch import FetchDrama, FetchPerson, FetchCast, FetchReviews


def error(code: int, description: str) -> Dict[str, Any]:
    return {
        "error": True,
        "code": code,
        "description": "404 Not Found"
        if code == 404
        else description,  # prioritize error 404
    }


# search function
def search_func(query: str) -> Dict[str, Any]:
    f = Search.scrape(query=query, t="search")
    if not f.ok:
        return error(f.status_code, "An unexpected error occurred.")
    else:
        f._get_search_results()

    return f.search()


fs = {
    "drama": FetchDrama,
    "person": FetchPerson,
    "cast": FetchCast,
    "reviews": FetchReviews,
}


# fetch function
def fetch_func(query: str, t: str) -> Dict[str, Any]:
    if t not in fs.keys():
        raise Exception("Invalid Error")

    f = fs[t].scrape(query=query, t="page")
    if not f.ok:
        return error(f.status_code, "An unexpected error occurred.")
    else:
        f._get()

    return f.fetch()