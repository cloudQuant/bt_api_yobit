from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class YobitExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = 'YOBIT'


class YobitExchangeDataSpot(YobitExchangeData):
    _REST_URL = 'https://yobit.net'
    _WSS_URL = 'wss://ws.yobit.net'
    _KLINE_PERIODS = {
        '1m': '1',
        '5m': '5',
        '15m': '15',
        '30m': '30',
        '1h': '60',
        '4h': '240',
        '1d': '1440',
    }
    _REST_PATHS = {
        'ticker': '/api/3/ticker/{symbol}',
        'depth': '/api/3/depth/{symbol}',
        'trades': '/api/3/trades/{symbol}',
        'info': '/api/3/info',
        'account': '/keyed',
    }

    def __init__(self) -> None:
        super().__init__()
        self.rest_url = self._REST_URL
        self.wss_url = self._WSS_URL
        self.kline_periods = dict(self._KLINE_PERIODS)
        self.rest_paths = dict(self._REST_PATHS)

    def get_rest_url(self) -> str:
        return self.rest_url

    def get_wss_url(self) -> str:
        return self.wss_url

    def get_kline_periods(self) -> dict[str, str]:
        return dict(self.kline_periods)

    def get_symbol(self, symbol: str) -> str:
        return symbol.lower()

    def get_rest_path(self, action: str) -> str:
        return self.rest_paths.get(action, '')

    def get_wss_path(self, action: str) -> str:
        return ''

    def get_local_symbol(self, symbol: str) -> str:
        return symbol.upper()

    def is_trading_enabled(self) -> bool:
        return True
