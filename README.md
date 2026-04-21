# bt_api_yobit

YoBit exchange adapter for bt_api.

## Installation

```bash
pip install bt_api_yobit
```

## Usage

```python
from bt_api_yobit import register_yobit
register_yobit()

from bt_api_py import BtApi
api = BtApi(exchange_kwargs={"YOBIT___SPOT": {"api_key": "...", "secret": "..."}})
ticker = api.get_tick("YOBIT___SPOT", "btc_usdt")
```
