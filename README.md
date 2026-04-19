<div align="center">

<img align="center" src=figs/logo_transparent_background.png width="55%"/>

# FinRL: Financial Reinforcement Learning

### *Deep Reinforcement Learning Framework for Automated Quantitative Trading*

> A production-ready DRL framework for financial trading — covering data acquisition, model training, backtesting, and live paper trading across stocks, crypto, and portfolios.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/finrl.svg)](https://pypi.org/project/finrl/)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Supported Data Sources](#-supported-data-sources)
- [Installation](#-installation)
- [Quick Start Tutorial](#-quick-start-tutorial)
- [API Reference](#-api-reference)
- [Notes & Recommendations](#-notes--recommendations)
- [License](#-license)

---

## 🧠 About the Project

**FinRL** is a deep reinforcement learning framework for automated quantitative trading. It provides end-to-end support for the full trading pipeline — from market data acquisition and feature engineering to model training, backtesting, and live paper trading.

The framework is designed around three core layers:

- 🏛️ **Market Environments** — Gym-style environments for stocks, crypto, and portfolios
- 🤖 **DRL Agents** — Plug-and-play support for ElegantRL, RLlib, and Stable Baselines 3
- 📊 **Financial Applications** — Ready-to-use trading strategies and backtesting pipelines

Whether you're a researcher prototyping new trading strategies or a developer building production trading systems — **FinRL provides the foundation.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧪 **Multi-Agent Training** | Train 5 DRL agents simultaneously: A2C, DDPG, PPO, TD3, SAC |
| 📈 **Backtesting Engine** | Compare agent performance against MVO and market index baselines |
| 📡 **14+ Data Sources** | Yahoo Finance, Alpaca, Binance, WRDS, CCXT, and more |
| 🔧 **Technical Indicators** | Built-in MACD, RSI, Bollinger Bands, CCI, SMA via stockstats |
| 💹 **Multi-Asset Support** | Stocks, cryptocurrencies, forex, and portfolio allocation |
| 🏋️ **Gym-Style Environments** | OpenAI Gymnasium-compatible market environments |
| 📱 **Paper Trading** | Live paper trading integration with Alpaca API |
| 🧮 **Ensemble Strategies** | Combine multiple agents for robust trading decisions |

---

## 🏗️ Architecture

The framework follows a **train → test → trade** pipeline:

```
Data Acquisition → Feature Engineering → Environment Setup → Agent Training → Backtesting → Paper Trading
```

**Three-Layer Design:**

1. **Application Layer** — Stock trading, portfolio allocation, crypto trading, HFT
2. **Agent Layer** — ElegantRL, RLlib, Stable Baselines 3 algorithms
3. **Environment Layer** — Market data processors, gym environments, preprocessors

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.7+** | Core language |
| **Stable Baselines 3** | Primary DRL algorithm library |
| **ElegantRL** | Lightweight DRL algorithms |
| **Ray/RLlib** | Scalable distributed RL |
| **Gymnasium** | Environment interface |
| **yfinance** | Market data (Yahoo Finance) |
| **Alpaca API** | Paper/live trading |
| **stockstats** | Technical indicators |
| **Matplotlib / Recharts** | Visualization and plotting |
| **pandas / numpy** | Data manipulation |

---

## 📁 Project Structure

```
Finance_pro/
├── finrl/                          # Core library
│   ├── applications/              # Trading task implementations
│   │   ├── cryptocurrency_trading/
│   │   ├── high_frequency_trading/
│   │   ├── portfolio_allocation/
│   │   └── stock_trading/
│   ├── agents/                    # DRL algorithm integrations
│   │   ├── elegantrl/
│   │   ├── rllib/
│   │   └── stablebaseline3/
│   ├── meta/                      # Market environments & data
│   │   ├── data_processors/
│   │   ├── env_cryptocurrency_trading/
│   │   ├── env_portfolio_allocation/
│   │   ├── env_stock_trading/
│   │   ├── preprocessor/
│   │   └── data_processor.py
│   ├── config.py                  # Global configuration
│   ├── config_tickers.py          # Ticker lists (DOW 30, NASDAQ, etc.)
│   ├── main.py                    # CLI entry point
│   ├── train.py                   # Training pipeline
│   ├── test.py                    # Testing pipeline
│   ├── trade.py                   # Live trading pipeline
│   └── plot.py                    # Visualization utilities
│
├── examples/                      # Tutorial scripts
│   ├── FinRL_StockTrading_2026_1_data.py
│   ├── FinRL_StockTrading_2026_2_train.py
│   └── FinRL_StockTrading_2026_3_Backtest.py
│
├── unit_tests/                    # Test suite
├── docs/                          # Documentation (Sphinx)
├── docker/                        # Docker configuration
├── figs/                          # Diagrams and figures
├── setup.py                       # Package setup
├── pyproject.toml                 # Poetry configuration
├── requirements.txt               # Dependencies
└── README.md
```

---

## 📡 Supported Data Sources

| Data Source | Type | Range & Frequency | Raw Data | Preprocessed Data |
|---|---|---|---|---|
| [YahooFinance](https://pypi.org/project/yfinance/) | US Securities | Frequency-specific, 1min | OHLCV | Prices & Indicators |
| [Alpaca](https://docs.alpaca.markets/) | US Stocks, ETFs | 2015-now, 1min | OHLCV | Prices & Indicators |
| [Binance](https://binance-docs.github.io/) | Cryptocurrency | API-specific, 1s | OHLCV | Prices & Indicators |
| [CCXT](https://docs.ccxt.com/) | Cryptocurrency | API-specific, 1min | OHLCV | Prices & Indicators |
| [WRDS](https://wrds-www.wharton.upenn.edu/) | US Securities | 2003-now, 1ms | Intraday Trades | Prices & Indicators |
| [Akshare](https://alpaca.markets/) | CN Securities | 2015-now, 1day | OHLCV | Prices & Indicators |
| [Baostock](http://baostock.com/) | CN Securities | 1990-now, 5min | OHLCV | Prices & Indicators |
| [IEXCloud](https://iexcloud.io/) | NMS US Securities | 1970-now, 1day | OHLCV | Prices & Indicators |
| [JoinQuant](https://www.joinquant.com/) | CN Securities | 2005-now, 1min | OHLCV | Prices & Indicators |
| [QuantConnect](https://www.quantconnect.com/) | US Securities | 1998-now, 1s | OHLCV | Prices & Indicators |
| [Tushare](https://tushare.pro/) | CN Securities | -now, 1min | OHLCV | Prices & Indicators |
| [Sinopac](https://sinotrade.github.io/) | Taiwan Securities | 2023-now, 1min | OHLCV | Prices & Indicators |

> **OHLCV:** Open, High, Low, Close prices + Volume
>
> **Technical Indicators:** MACD, Bollinger Bands, RSI, CCI, DX, SMA (30/60 day)

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip or [Poetry](https://python-poetry.org/)

### Option 1: Install from Source

```bash
git clone <your-repo-url>
cd Finance_pro
python -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate     # Windows
pip install -e .
```

### Option 2: Install via pip

```bash
pip install finrl
```

### Option 3: Docker

```bash
cd docker
bash bin/build_container.sh
```

---

## 📖 Quick Start Tutorial

### Step 1: Set Up the Environment

```bash
cd Finance_pro
python -m venv venv
venv\Scripts\activate        # Windows
pip install -e .
```

### Step 2: Download & Preprocess Data

```bash
python examples/FinRL_StockTrading_2026_1_data.py
```

This downloads DOW 30 stock data from Yahoo Finance, adds technical indicators (MACD, RSI, etc.), VIX, and turbulence index, then splits into training (2014–2025) and trading (2026) sets.

### Step 3: Train DRL Agents

```bash
python examples/FinRL_StockTrading_2026_2_train.py
```

Trains 5 DRL agents (A2C, DDPG, PPO, TD3, SAC) using Stable Baselines 3. Models are saved to `trained_models/`.

**Key Hyperparameters:**

| Parameter | Description | Default |
|---|---|---|
| `total_timesteps` | Total environment interactions for training | 20,000 |
| `learning_rate` | Weight update step size | 0.001 |
| `batch_size` | Samples per gradient update | 100 |
| `buffer_size` | Replay buffer capacity (off-policy) | 1,000,000 |

### Step 4: Backtest

```bash
python examples/FinRL_StockTrading_2026_3_Backtest.py
```

Runs trained agents on trading data and compares against MVO and DJIA baselines. Results are printed to console and saved as `backtest_result.png`.

---

## 📡 API Reference

### Configuration (`finrl/config.py`)

| Variable | Default | Description |
|---|---|---|
| `TRAIN_START_DATE` | `2014-01-06` | Training period start |
| `TRAIN_END_DATE` | `2025-12-31` | Training period end |
| `TRADE_START_DATE` | `2026-01-01` | Trading/test period start |
| `TRADE_END_DATE` | `2026-03-20` | Trading/test period end |
| `INDICATORS` | MACD, RSI, Bollinger, etc. | Technical indicators to compute |

### DRL Agent Parameters

| Agent | Key Parameters |
|---|---|
| **A2C** | `n_steps=5`, `ent_coef=0.01`, `lr=0.0007` |
| **PPO** | `n_steps=2048`, `batch_size=64`, `lr=0.00025` |
| **DDPG** | `batch_size=128`, `buffer_size=50k`, `lr=0.001` |
| **TD3** | `batch_size=100`, `buffer_size=1M`, `lr=0.001` |
| **SAC** | `batch_size=64`, `buffer_size=100k`, `lr=0.0001` |

---

## 📝 Notes & Recommendations

- **API Keys** — Set your Alpaca, Binance, or other API keys in `finrl/config.py` or via environment variables. Never commit secrets.
- **Training Time** — Start with low `total_timesteps` (1,000) to verify the pipeline works, then scale up (100k+) for serious training.
- **GPU Support** — Stable Baselines 3 supports CUDA. Install PyTorch with GPU support for faster training.
- **Data Quality** — Yahoo Finance is free but has limitations. For institutional-grade data, use WRDS or Alpaca.
- **Backtesting** — Always backtest before paper/live trading. Compare against multiple baselines.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**Disclaimer: This software is for educational and research purposes only. Nothing herein constitutes financial advice or a recommendation to trade real money. Users are solely responsible for any financial decisions made using this software. Consult a qualified professional before deploying capital.**

---

<div align="center">

Built by **Digital Metro** 🚀

</div>
