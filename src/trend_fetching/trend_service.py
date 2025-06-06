from typing import List, Dict, Any, Optional
import logging
from dataclasses import dataclass
from enum import Enum, auto

class TrendSource(Enum):
    TWITTER = auto()
    REDDIT = auto()
    COINMARKETCAP = auto()

@dataclass
class TrendData:
    """
    Represents a single trend data point with comprehensive metadata.
    """
    source: TrendSource
    topic: str
    relevance_score: float
    volume: int
    timestamp: str
    additional_context: Optional[Dict[str, Any]] = None

class TrendFetchingService:
    """
    A flexible service for fetching and processing cryptocurrency trends.
    
    Supports multiple data sources with configurable fetching strategies.
    """
    
    def __init__(self, sources: List[TrendSource] = None, 
                 config: Optional[Dict[str, Any]] = None):
        """
        Initialize the trend fetching service.
        
        Args:
            sources: List of trend sources to fetch from. 
                     Defaults to all available sources if not specified.
            config: Optional configuration dictionary for customizing service behavior.
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.sources = sources or list(TrendSource)
        self.config = config or {}
        self._validate_config()
    
    def _validate_config(self):
        """
        Validate and sanitize configuration parameters.
        Raises ValueError for invalid configurations.
        """
        # Basic config validation
        max_results = self.config.get('max_results', 10)
        if not isinstance(max_results, int) or max_results <= 0:
            raise ValueError("max_results must be a positive integer")
    
    def fetch_trends(self, timeframe: str = '24h') -> List[TrendData]:
        """
        Fetch trends from configured sources.
        
        Args:
            timeframe: Time period for trend analysis (e.g., '24h', '7d')
        
        Returns:
            List of trend data points, sorted by relevance score
        """
        trends = []
        
        try:
            for source in self.sources:
                source_trends = self._fetch_from_source(source, timeframe)
                trends.extend(source_trends)
        except Exception as e:
            self.logger.error(f"Error fetching trends: {e}")
            # Graceful degradation: return partial results
        
        # Sort trends by relevance score in descending order
        return sorted(trends, key=lambda x: x.relevance_score, reverse=True)
    
    def _fetch_from_source(self, source: TrendSource, timeframe: str) -> List[TrendData]:
        """
        Internal method to fetch trends from a specific source.
        
        Args:
            source: The trend source to fetch from
            timeframe: Time period for trend analysis
        
        Returns:
            List of trend data points from the specified source
        """
        # Simulated trend fetching - to be replaced with actual API integrations
        mock_trends = {
            TrendSource.TWITTER: [
                TrendData(
                    source=TrendSource.TWITTER,
                    topic='Bitcoin Price Surge',
                    relevance_score=0.85,
                    volume=5000,
                    timestamp='2024-01-15T12:00:00Z'
                )
            ],
            TrendSource.REDDIT: [
                TrendData(
                    source=TrendSource.REDDIT,
                    topic='Ethereum Layer 2 Solutions',
                    relevance_score=0.75,
                    volume=3500,
                    timestamp='2024-01-15T12:00:00Z'
                )
            ],
            TrendSource.COINMARKETCAP: [
                TrendData(
                    source=TrendSource.COINMARKETCAP,
                    topic='DeFi Token Performance',
                    relevance_score=0.65,
                    volume=2800,
                    timestamp='2024-01-15T12:00:00Z'
                )
            ]
        }
        
        return mock_trends.get(source, [])