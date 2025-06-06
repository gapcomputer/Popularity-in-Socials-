import pytest
from src.trend_fetching.trend_service import (
    TrendFetchingService, 
    TrendSource, 
    TrendData
)

def test_trend_service_initialization():
    """Test basic initialization of TrendFetchingService."""
    service = TrendFetchingService()
    assert len(service.sources) == 3  # All sources by default
    assert all(source in TrendSource for source in service.sources)

def test_trend_service_custom_sources():
    """Test initializing service with custom sources."""
    custom_sources = [TrendSource.TWITTER, TrendSource.REDDIT]
    service = TrendFetchingService(sources=custom_sources)
    assert set(service.sources) == set(custom_sources)

def test_trend_service_fetch_trends():
    """Test fetching trends from service."""
    service = TrendFetchingService()
    trends = service.fetch_trends()
    
    assert len(trends) > 0
    assert all(isinstance(trend, TrendData) for trend in trends)
    
    # Check sorting by relevance score
    assert trends == sorted(trends, key=lambda x: x.relevance_score, reverse=True)

def test_trend_service_config_validation():
    """Test configuration validation."""
    # Valid configuration
    service = TrendFetchingService(config={'max_results': 5})
    assert service.config.get('max_results') == 5

    # Invalid configuration
    with pytest.raises(ValueError):
        TrendFetchingService(config={'max_results': -1})
    
    with pytest.raises(ValueError):
        TrendFetchingService(config={'max_results': 'invalid'})