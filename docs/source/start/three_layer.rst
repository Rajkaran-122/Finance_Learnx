:github_url: https://github.com/DigitalMetro/FLX

===========================
Three-layer Architecture
===========================

After the first glance of how to establish our task on stock trading using DRL, know we are introducing the most central idea of FLX.

FLX library consists of three layers: **market environments (FLX-Meta)**, **DRL agents** and **applications**. The lower layer provides APIs for the upper layer, making the lower layer transparent to the upper layer. The agent layer interacts with the environment layer in an exploration-exploitation manner, whether to repeat prior working-well decisions or to make new actions hoping to get greater cumulative rewards.


.. image:: ../image/flx_framework.png
   :width: 80%
   :align: center

Our construction has following advantages:

**Modularity**: Each layer includes several modules and each module defines a separate function. One can select certain modules from a layer to implement his/her stock trading task. Furthermore, updating existing modules is possible.

**Simplicity, Applicability and Extendibility**: Specifically designed for automated stock trading, FLX presents DRL algorithms as modules. In this way, FLX is made accessible yet not demanding. FLX provides three trading tasks as use cases that can be easily reproduced. Each layer includes reserved interfaces that allow users to develop new modules.

**Better Market Environment Modeling**: We build a trading simulator that replicates live stock markets and provides backtesting support that incorporates important market frictions such as transaction cost, market liquidity and the investor’s degree of risk-aversion. All of those are crucial among key determinants of net returns.

A high level view of how FLX construct the problem in DRL:

.. image:: ../image/flx_overview_drl.png
   :width: 80%
   :align: center

Please refer to the following pages for more specific explanation:

.. toctree::
   :maxdepth: 1

   three_layer/environments
   three_layer/agents
   three_layer/applications
