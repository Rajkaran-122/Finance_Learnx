## FinRL Core Library

This folder contains the core library organized into three subfolders:

+ **applications/** — Trading task implementations (stock trading, crypto, portfolio allocation, HFT)
+ **agents/** — DRL algorithm integrations from ElegantRL, RLlib, and Stable Baselines 3. Users can plug in any DRL library.
+ **meta/** — Market environments and data processors for gym-style financial environments.

The framework employs a **train → test → trade** pipeline through three files: `train.py`, `test.py`, and `trade.py`.

```
finrl/
├── applications/
│   ├── cryptocurrency_trading/
│   ├── high_frequency_trading/
│   ├── portfolio_allocation/
│   └── stock_trading/
├── agents/
│   ├── elegantrl/
│   ├── rllib/
│   └── stablebaseline3/
├── meta/
│   ├── data_processors/
│   ├── env_cryptocurrency_trading/
│   ├── env_portfolio_allocation/
│   ├── env_stock_trading/
│   ├── preprocessor/
│   ├── data_processor.py
│   └── finrl_meta_config.py
├── config.py
├── config_tickers.py
├── main.py
├── train.py
├── test.py
├── trade.py
└── plot.py
```
