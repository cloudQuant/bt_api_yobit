# YOBIT

Exchange plugin for bt_api framework — Russian cryptocurrency exchange.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_yobit.svg)](https://pypi.org/project/bt_api_yobit/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_yobit.svg)](https://pypi.org/project/bt_api_yobit/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_yobit/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_yobit/actions)
[![Docs](https://readthedocs.org/projects/bt-api-yobit/badge/?version=latest)](https://bt-api-yobit.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

[YoBit](https://yobit.net/) is a **Russian cryptocurrency exchange** offering trading services with a wide range of altcoins. This plugin integrates YoBit into the [bt_api](https://github.com/cloudQuant/bt_api_py) unified trading framework, supporting **SPOT** markets.

### Features

- **REST API** — market data queries, order management, account queries
- **Wide altcoin coverage** — supports many small-cap trading pairs
- **Simple API key auth** — standard API key + secret authentication

### Exchange Code

| Code | Description | Asset Type |
|------|-------------|------------|
| `YOBIT___SPOT` | YoBit spot markets | SPOT |

### Installation

```bash
pip install bt_api_yobit
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_yobit
cd bt_api_yobit
pip install -e .
```

### Quick Start

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "YOBIT___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker data
ticker = api.get_tick("YOBIT___SPOT", "BTC_USDT")
print(ticker)

# Get order book
depth = api.get_depth("YOBIT___SPOT", "BTC_USDT", count=20)
print(depth)

# Get klines
bars = api.get_kline("YOBIT___SPOT", "BTC_USDT", period="1h", count=100)
print(bars)
```

### Supported Operations

| Operation | Status | Description |
|-----------|--------|-------------|
| Ticker | ✅ | Real-time price and 24h statistics |
| OrderBook/Depth | ✅ | Market depth and order book |
| Klines/Bars | ✅ | Historical OHLCV data |
| Exchange Info | ✅ | Trading rules and symbol info |
| Balance | ✅ | Account balance queries |
| Account | ✅ | Account information |
| Make Order | ✅ | Place limit/market orders |
| Cancel Order | ✅ | Cancel existing orders |

### API Reference

#### Feed — YobitRequestDataSpot

Inherits from `YobitRequestData`. Access via `BtApi`.

```python
api.get_tick("YOBIT___SPOT", "BTC_USDT")       # Ticker
api.get_depth("YOBIT___SPOT", "BTC_USDT")      # Order book
api.get_kline("YOBIT___SPOT", "BTC_USDT")     # Klines
api.get_exchange_info("YOBIT___SPOT")          # Exchange info
```

#### Container — YobitExchangeDataSpot

Exchange metadata and configuration.

```python
from bt_api_yobit import YobitExchangeDataSpot

info = YobitExchangeDataSpot()
print(info.get_rest_url())    # https://yobit.net
print(info.get_wss_url())     # wss://ws.yobit.net
print(info.get_kline_periods())  # { "1m": "1", "5m": "5", ... }
```

#### REST Endpoints

| Action | Path | Method |
|--------|------|--------|
| ticker | `/api/3/ticker/{symbol}` | GET |
| depth | `/api/3/depth/{symbol}` | GET |
| trades | `/api/3/trades/{symbol}` | GET |
| info | `/api/3/info` | GET |
| account | `/keyed` | GET |

### Architecture

```
bt_api_yobit/
├── src/bt_api_yobit/
│   ├── containers/      # YobitExchangeDataSpot
│   ├── feeds/           # YobitRequestDataSpot
│   ├── exchange_data/    # Exchange metadata
│   ├── errors/          # Error translation
│   └── plugin.py        # register_yobit()
└── docs/
    └── index.md         # Bilingual API docs
```

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Online Documentation

| Resource | Link |
|----------|------|
| Full Docs | https://bt-api-yobit.readthedocs.io/ |
| Chinese Docs | https://bt-api-yobit.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_yobit |
| Issue Tracker | https://github.com/cloudQuant/bt_api_yobit/issues |

### License

MIT License — see [LICENSE](LICENSE) for details.

---

## 中文

### 概述

[YoBit](https://yobit.net/) 是一家 **俄罗斯加密货币交易所**，提供多种山寨币交易对。本插件将 YoBit 接入 [bt_api](https://github.com/cloudQuant/bt_api_py) 统一交易框架，支持 **现货 (SPOT)** 市场。

### 功能特点

- **REST API** — 行情查询、订单管理、账户查询
- **广泛的山寨币覆盖** — 支持大量小市值币种交易对
- **简单 API Key 认证** — 标准 API Key + Secret 认证方式

### 交易所代码

| 代码 | 描述 | 资产类型 |
|------|--------|----------|
| `YOBIT___SPOT` | YoBit 现货市场 | SPOT |

### 安装

```bash
pip install bt_api_yobit
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_yobit
cd bt_api_yobit
pip install -e .
```

### 快速开始

```python
from bt_api import BtApi

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
print(ticker)

# 获取订单簿
depth = api.get_depth("YOBIT___SPOT", "BTC_USDT", count=20)
print(depth)

# 获取K线
bars = api.get_kline("YOBIT___SPOT", "BTC_USDT", period="1h", count=100)
print(bars)
```

### 支持的操作

| 操作 | 状态 | 说明 |
|------|------|------|
| 行情 (Ticker) | ✅ | 实时价格和24小时统计 |
| 订单簿 (OrderBook) | ✅ | 市场深度和挂单 |
| K线 (Klines) | ✅ | 历史OHLCV数据 |
| 交易所信息 | ✅ | 交易规则和交易对信息 |
| 余额 (Balance) | ✅ | 账户余额查询 |
| 账户 (Account) | ✅ | 账户信息 |
| 下单 (Make Order) | ✅ | 限价/市价下单 |
| 撤单 (Cancel Order) | ✅ | 取消现有订单 |

### API 参考

#### Feed — YobitRequestDataSpot

继承自 `YobitRequestData`，通过 `BtApi` 访问。

```python
api.get_tick("YOBIT___SPOT", "BTC_USDT")        # 行情
api.get_depth("YOBIT___SPOT", "BTC_USDT")       # 订单簿
api.get_kline("YOBIT___SPOT", "BTC_USDT")       # K线
api.get_exchange_info("YOBIT___SPOT")            # 交易所信息
```

#### Container — YobitExchangeDataSpot

交易所元数据和配置。

```python
from bt_api_yobit import YobitExchangeDataSpot

info = YobitExchangeDataSpot()
print(info.get_rest_url())    # https://yobit.net
print(info.get_wss_url())    # wss://ws.yobit.net
print(info.get_kline_periods())  # { "1m": "1", "5m": "5", ... }
```

#### REST 端点

| 动作 | 路径 | 方法 |
|------|------|------|
| ticker | `/api/3/ticker/{symbol}` | GET |
| depth | `/api/3/depth/{symbol}` | GET |
| trades | `/api/3/trades/{symbol}` | GET |
| info | `/api/3/info` | GET |
| account | `/keyed` | GET |

### 项目结构

```
bt_api_yobit/
├── src/bt_api_yobit/
│   ├── containers/      # YobitExchangeDataSpot
│   ├── feeds/           # YobitRequestDataSpot
│   ├── exchange_data/    # 交易所元数据
│   ├── errors/          # 错误翻译
│   └── plugin.py        # register_yobit()
└── docs/
    └── index.md         # 中英文API文档
```

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 在线文档

| 资源 | 链接 |
|------|------|
| 完整文档 | https://bt-api-yobit.readthedocs.io/ |
| 中文文档 | https://bt-api-yobit.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_yobit |
| 问题反馈 | https://github.com/cloudQuant/bt_api_yobit/issues |

### 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。
