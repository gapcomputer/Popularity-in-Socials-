import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.trend_sourcer import TrendSourcer

def test_trend_sourcer_initialization():
    """Test that TrendSourcer can be initialized successfully."""
    sourcer = TrendSourcer()
    assert sourcer is not None

def test_aggregate_trends():
    """Test trend aggregation with sample keywords."""
    sourcer = TrendSourcer()
    keywords = ['Bitcoin', 'Ethereum']
    
    trends = sourcer.aggregate_trends(keywords)
    
    assert isinstance(trends, dict)
    assert len(trends) == 2
    
    for keyword in keywords:
        assert keyword in trends
        assert 0 <= trends[keyword] <= 1

def test_fetch_social_media_trends():
    """Test social media trend retrieval."""
    sourcer = TrendSourcer()
    keyword = 'Blockchain'
    
    trends = sourcer.fetch_social_media_trends(keyword)
    
    assert isinstance(trends, list)
    for trend in trends:
        assert 'platform' in trend
        assert 'relevance' in trend
        assert 'volume' in trend

@pytest.mark.parametrize("keywords", [
    ['Bitcoin'], 
    ['Ethereum', 'Blockchain'], 
    []
])
def test_trend_sourcing_variations(keywords):
    """Test trend sourcing with different keyword scenarios."""
    sourcer = TrendSourcer()
    trends = sourcer.aggregate_trends(keywords)
    
    if keywords:
        assert len(trends) == len(keywords)
    else:
        assert len(trends) == 0