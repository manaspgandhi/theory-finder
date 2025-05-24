from data_pipeline.reddit_scraper import search_reddit
from data_pipeline.quora_scraper import search_quora
from typing import List, Dict

def collect_theories(query: str) -> List[Dict]:
    """Collect theories from multiple sources given a query."""
    reddit_results = search_reddit(query)
    quora_results = search_quora(query)
    # TODO: Add more sources and aggregation logic
    return reddit_results + quora_results 