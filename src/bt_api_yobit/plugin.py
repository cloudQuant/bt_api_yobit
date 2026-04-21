from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry


def register_yobit() -> None:
    from bt_api_yobit.feeds.live_yobit.spot import YobitRequestDataSpot
    from bt_api_yobit.exchange_data import YobitExchangeDataSpot

    ExchangeRegistry.register_feed("YOBIT___SPOT", YobitRequestDataSpot)
    ExchangeRegistry.register_exchange_data("YOBIT___SPOT", YobitExchangeDataSpot)
    ExchangeRegistry.register_balance_handler("YOBIT___SPOT", simple_balance_handler)


def plugin_info() -> PluginInfo:
    from bt_api_yobit import __version__

    return PluginInfo(
        name="YoBit",
        version=__version__,
        core_requires="bt_api_base",
        supported_exchanges=("YOBIT___SPOT",),
        supported_asset_types=("SPOT",),
        plugin_module="bt_api_yobit",
    )
