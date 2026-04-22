# YOBIT API Reference

## English | [中文](#中文)

### Exchange Code

`YOBIT___SPOT`

### Exchange Info

| Item | Value |
|------|-------|
| REST URL | `https://yobit.net` |
| WebSocket URL | `wss://ws.yobit.net` |
| Asset Type | SPOT |
| Plugin Entry | `bt_api_yobit.plugin:register_yobit` |

### Supported Capabilities

| Capability | Supported |
|------------|-----------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |

### REST Endpoints

| Action | Path | Description |
|--------|------|-------------|
| ticker | `/api/3/ticker/{symbol}` | Price tickers for symbols |
| depth | `/api/3/depth/{symbol}` | Order book depth |
| trades | `/api/3/trades/{symbol}` | Recent trades |
| info | `/api/3/info` | Exchange trading rules and info |
| account | `/keyed` | Authenticated account info |

### Kline Periods

| Period | YoBit Value |
|--------|-------------|
| 1m | 1 |
| 5m | 5 |
| 15m | 15 |
| 30m | 30 |
| 1h | 60 |
| 4h | 240 |
| 1d | 1440 |

### API Usage

```python
from bt_api import BtApi

# Initialize
api = BtApi(
    exchange_kwargs={
        "YOBIT___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker
ticker = api.get_tick("YOBIT___SPOT", "BTC_USDT")

# Get depth
depth = api.get_depth("YOBIT___SPOT", "BTC_USDT", count=20)

# Get klines
bars = api.get_kline("YOBIT___SPOT", "BTC_USDT", period="1h", count=100)

# Get balance
balance = api.get_balance("YOBIT___SPOT")

# Place order
order = api.make_order("YOBIT___SPOT", "BTC_USDT", volume=0.001, price=50000, order_type="limit")

# Cancel order
api.cancel_order("YOBIT___SPOT", "BTC_USDT", order_id="your_order_id")
```

### Container — YobitExchangeDataSpot

```python
from bt_api_yobit import YobitExchangeDataSpot

info = YobitExchangeDataSpot()
print(info.get_rest_url())          # https://yobit.net
print(info.get_wss_url())           # wss://ws.yobit.net
print(info.get_kline_periods())     # { "1m": "1", "5m": "5", ... }
print(info.get_rest_path("ticker")) # /api/3/ticker/{symbol}
print(info.get_symbol("BTC_USDT"))  # btc_usdt
print(info.get_local_symbol("btc_usdt"))  # BTC_USDT
```

---

## 中文

### 交易所代码

`YOBIT___SPOT`

### 交易所信息

| 项目 | 值 |
|------|-----|
| REST URL | `https://yobit.net` |
| WebSocket URL | `wss://ws.yobit.net` |
| 资产类型 | SPOT |
| 插件入口 | `bt_api_yobit.plugin:register_yobit` |

### 支持的能力

| 能力 | 支持状态 |
|------|---------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |

### REST 端点

| 动作 | 路径 | 说明 |
|------|------|------|
| ticker | `/api/3/ticker/{symbol}` | 交易对价格行情 |
| depth | `/api/3/depth/{symbol}` | 订单簿深度 |
| trades | `/api/3/trades/{symbol}` | 最近成交 |
| info | `/api/3/info` | 交易所交易规则和信息 |
| account | `/keyed` | 认证账户信息 |

### K线周期

| 周期 | YoBit 值 |
|------|---------|
| 1m | 1 |
| 5m | 5 |
| 15m | 15 |
| 30m | 30 |
| 1h | 60 |
| 4h | 240 |
| 1d | 1440 |

### API 用法

```python
from bt_api import BtApi

# 初始化
api = BtApi(
    exchange_kwargs={
        "YOBIT___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# 获取行情
ticker = api.get_tick("YOBIT___SPOT", "BTC_USDT")

# 获取深度
depth = api.get_depth("YOBIT___SPOT", "BTC_USDT", count=20)

# 获取K线
bars = api.get_kline("YOBIT___SPOT", "BTC_USDT", period="1h", count=100)

# 获取余额
balance = api.get_balance("YOBIT___SPOT")

# 下单
order = api.make_order("YOBIT___SPOT", "BTC_USDT", volume=0.001, price=50000, order_type="limit")

# 撤单
api.cancel_order("YOBIT___SPOT", "BTC_USDT", order_id="your_order_id")
```

### 容器类 — YobitExchangeDataSpot

```python
from bt_api_yobit import YobitExchangeDataSpot

info = YobitExchangeDataSpot()
print(info.get_rest_url())          # https://yobit.net
print(info.get_wss_url())           # wss://ws.yobit.net
print(info.get_kline_periods())      # { "1m": "1", "5m": "5", ... }
print(info.get_rest_path("ticker")) # /api/3/ticker/{symbol}
print(info.get_symbol("BTC_USDT"))  # btc_usdt
print(info.get_local_symbol("btc_usdt"))  # BTC_USDT
```
