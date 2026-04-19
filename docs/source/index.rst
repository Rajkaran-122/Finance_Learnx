.. FinRL Library documentation

Welcome to FinRL Library!
=====================================================================================================

.. meta::
   :description: FinRL is an open source framework for financial reinforcement learning. It facilitates development of stock trading strategies using deep reinforcement learning, providing fine-tuned algorithms including DQN, DDPG, PPO, SAC, A2C, TD3, etc.
   :keywords: finance AI, artificial intelligence in finance, machine learning, deep reinforcement learning, DRL, RL, neural networks, deep q network, quantitative trading

.. image:: image/logo_transparent_background.png

**Disclaimer: Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**

FinRL is an open source framework for financial reinforcement learning, providing end-to-end support for automated quantitative trading.

Reinforcement learning (RL) trains an agent to solve tasks by trial and error, while DRL uses deep neural networks as function approximators. DRL balances exploration (of uncharted territory) and exploitation (of current knowledge), and has been recognized as a competitive edge for automated trading. DRL framework is powerful in solving dynamic decision making problems by learning through interactions with an unknown environment, thus exhibiting two major advantages: portfolio scalability and market model independence. Automated trading is essentially making dynamic decisions, namely **to decide where to trade, at what price, and what quantity**, over a highly stochastic and complex stock market. Taking many complex financial factors into account, DRL trading agents build a multi-factor model and provide algorithmic trading strategies, which are difficult for human traders.

FinRL provides a framework that supports various markets, SOTA DRL algorithms, benchmarks of many quant finance tasks, live trading, etc.

|

.. toctree::
   :maxdepth: 1
   :hidden:

   Home <self>


.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   start/introduction
   start/first_glance
   start/three_layer
   start/installation
   start/quick_start


.. toctree::
   :maxdepth: 1
   :caption: FinRL-Meta

   finrl_meta/background
   finrl_meta/overview
   finrl_meta/Data_layer
   finrl_meta/Environment_layer
   finrl_meta/Benchmark


.. toctree::
   :maxdepth: 3
   :caption: Tutorials

   tutorial/Guide
   tutorial/Homegrown_example
   tutorial/1-Introduction
   tutorial/2-Advance
   tutorial/3-Practical
   tutorial/4-Optimization
   tutorial/5-Others


.. toctree::
   :maxdepth: 1
   :caption: Developer Guide

   developer_guide/file_architecture
   developer_guide/development_setup
   developer_guide/contributing


.. toctree::
   :maxdepth: 1
   :caption: Reference

   reference/publication
   reference/reference.md


.. toctree::
   :maxdepth: 2
   :caption: FAQ

   faq
