import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views.viewer_id == views.author_id]
    views = views[["viewer_id"]].rename(columns={"viewer_id": "id"}).drop_duplicates()
    views = views.sort_values(by ="id", ascending=True)
    return views