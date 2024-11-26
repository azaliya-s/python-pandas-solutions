# Article Views I
# Write a solution to find all the authors that viewed at least one of their own articles. Return the result table sorted by id in ascending order.
# Solution for the 'Article Views I' problem.
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    viewed = views[views['author_id'] == views['viewer_id']][['author_id']].rename(columns={'author_id': 'id'})
    sorted_viewed = viewed.sort_values(by = 'id').drop_duplicates()
    return sorted_viewed
