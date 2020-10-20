# Mantis Trading
## Version 1.2

### Sub Projects
    1. Crypto Trading System: An algorithmic trading engine built for easy strategy research, backtesting and live trading on the KuCoin Crypto Trading Exchange. 

### Social
[Shrimpy Referral Link](https://shrimpy.io/referral?r=6J9tbEvsZ)  
[Shrimpy Linked In](https://www.linkedin.com/company/shrimpy/)  


### Ethos/Missions
    - maximize Risk-Adjusted Returns relative to BTC
    - accumulate bitcoin for our families
    - to maximize our positive impact on society
    - to accelerate the adoption of digital assets
    

### Tools
    - GITLAB- AGILE PROJECT MANAGEMENT TOOL
    - SHRIMPY DEVELOPER API- Crypto Trading API for historical data(OHLCV), universal web-sockets, low latency order execution, portfolio management, managing accounts and users, infrastructure and scalability, exchange Management.
    - SHRIMPY- Social Trading Platform 
    - KUCOIN- Crypto Exchange
    - PYTHON- Object Oriented Programming Language
    - PYTHON LIBRARIES
        - Pandas 
        - Numpy
        - sci-kit learn
        - tensorflow
        - matplotlib
        
### MAJOR ASSUMPTIONS
    - when Bitcoin is in a bull market, altcoins outperform Bitcoin relative to the USD
    - when Bitcoin is in a bear market, altcoins underperform 
    - SHRIMPY DEVELOPER API can Scale with our ALGORITHMIC TRADING APPLICATION
    - GITLAB can serve as an efficient Project management tool
    - WE Can get all the historical data we need from Shrimpy dev api
    - KuCoin gives us biggest universe of digital assets to trade from
    - momentum strategies are more successful than mean reversion in the crypto markets
    - Measuring OHLCV instead of tick-data is efficient for rolling calculus measurements
    - We are building this engine for Quant Researchers/Traders, Crypto-Investors, and potentially license to prop trading firms

### TRADING Constraints
    - Inital Investment must be in-kind (BTC Transfer)
    - exchange = KuCoin
    - trading_fees = maximum fee
    - TRADING Spot Prices only
    - tax_rate = 30% on short term capital gains
        
### Milestones 
    1. DATA PRE-PROCESSING- FACTOR DATAFRAMES
        - btc_usd_6h
        - alt_btc_15 (450)
        - alt_btc_1h (450)
    2. FEATURE ENGINEERING- ML RESEARCH
        - features = rolling price velocities and accelerations
        - models = rnn, ann, lstm, gradient_boost, xg_boost, shapley, etc..
        - output = [price_predictions, bucket_classifications]
    3. OFFLINE ALGORITHMS- VECTORIZED BACKTEST FOR ALPHA
        - alpha_modeling.py
            - 3 layer allocation Model
                - Tide = technical analysis to determine bitcoin's trend
                - wave = [btc, usd, alt] rebalance to thresholds every 6h
                - ripple = [top 10 alts] rebalance to thresholds every 1h
               
        - run_backtest.py
            - maximize risk-adjusted returns relative to BTC
    4. ONLINE ALGORITHMS- SYSTEMIZE REAL-TIME TRADING
           - live_main.py
               - log.py
                   - trades.py
                   - orders.py
                   - capital_gains.py
                   - kpis.py
               - alerts.py
                   - reports.py (every 6 hrs)
                   - wins.py
                   - risk_thresholds.py
                   - kill_switch.py                  
               - models.py
                   - alpha_model.py
                   - portfolio_construction.py
                   - universe_selection.py
                   - execution.py
           
        - docker_container 
    5. PERFORMANCE DASHBOARD- REAL-TIME VISUALIZATIONS
        - real_time_performance_dash.py
        
    6. PUTTING IT ALL TOGETHER
        - HOME OFFICE DEPLOYMENT
        - Presentation
            - ASK?- License, investment,  



### AGILE PROJECT MANAGEMENT (SPRINT MEETING)
    1. Walk Through Product Roadmap (Milestones)
    2. Groom your Product Backlog and Update User Stories
        - Prioritize Roadmap
        - User Stories (break down user stories into technical tasks)
             - Researcher/Trader
                 - non-discolusure agreement
                 - compensation agreement
             - Investor
                 - limited partner agreement or terms of service for portfolio management capabilities or just use social trading
             - Licensee
                 - licensing terms of service agreement
                 - intellectual property agreement or copyright contract
    3.Sprint Goal: Deployable Crypto-Trading-System by Oct 3, 2020
    4. Capacity Planning 
        - Total Capacity = 5 teammembers x 4hours/day x 9days = 180 man hours
            - Scrum: 135 hours
            - Bug fixes: 45 hours
        - 25% of Resources should go to bug fixes during sprint
    5. Walk through User Stories and declar
        - Describe Technical tasks
        - Prioritize Tasks

### Improvement Proposals
    - Extend to Margin Trading and Futures Trading
    - Add More Accounts
    - Scale Trading App for Maximum Users
    - Use Tick Data instead of Candles for better algos
    - Cluster Analysis 

---
# PROFESSIONAL POSITIONING
### Differentials
    1. Phenomana
        - antifragility: Lose small, win big
        - law of large numbers: high frequency x expectedreturn>50% = profits
        - conservation of angular momentum, energy (Tide, wave, ripple)
        - entropy: 
        - CLT:
        - Deep Learning: 
    2. Risk Management
        - Dynamic Rebalance- multi-timeframe, multi-signal, thresholds
        - BTC Accumulator- Measure Performance against BTC
    3. Strategies
        - Crypto Trading
            - crypto_calculus: 
            - btc_accumulator: Every 6 hours rebalance thresholds and ammass BTC
    4. Team
        - Direction of Team
        - Values of Team
        - Skills of Team
        - Experiences of Team
        - Historical Success
    5. Technology
        - Programming
            - Python, pandas, matplotlib, api interactions
        - ML Applications
            - algorithmic trading
            - financial modeling, forecasting
        - ML Engineering skills
            - ML Algos: xg boost, lstm, gradient_boost, shapley, gri
            - ML Frameworks: tensorflow, keras, pytorch
        - Gitlab
           - Agile Project Management





---

## Gitlab Organization
Group: MANTIS TRADING
Project: Crypto Trading System
        
### Repository Organization
    - Custom Data Sets
        - historical_btc_factors.csv
        - historical_kucoin_factors.csv
    - Research Notebooks
        - RNN, CNN, ANN
        - gradientbooster.ipynb
        - XGboost.ipynb
        - LSTM.ipynb
        - Shapley.ipynb
    - Offline algorithm development
        - alpha_modeling.ipynb
        - backtester.ipynb
    - Online algorithm
        - live_trader.py
    - Realtime Performance Dashboard
        - dashboard.py
        - alerts.py
        
        
        
### PROJECT WIKI

#### Resources Page

#### PROJECT INSPIRATIONS
[Nomics](https://nomics.com)  
[strix leviathon- OCTOPUS](https://strixleviathan.com/crypto-fund-platform)  






#### Northwestern Fintech Resources

[NU Fintech Project 1: A Quantitative Trading System](https://github.com/gdepalma93/quantitative_trading_system)  
[NU Fintech Curriculum](https://media.trilogyed.com/Northwestern/pdf/fintech/NU_FinTech_curriculum_102419.pdf)  
[LSTM Predictor Hw solution](https://www.youtube.com/watch?v=7zwCrBMwIUA&feature=youtu.be)  


#### Machine Learning Resources
---
[problem formulation](https://developers.google.com/machine-learning/problem-framing/formulate)
[python pandas multiindexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)
[iterate over rows in pandas](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)   
[l1 and l2 regularization methods](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)   
[stock prediction: random forest regressor](https://github.com/ThomasRochefortB/SP1500stockPicker/blob/master/SP1500stockPicker.ipynb)    
[regularization methods](https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3) 
[lasso, ridge, elastic net ML](https://www.geeksforgeeks.org/lasso-vs-ridge-vs-elastic-net-ml/)   
[nueral networks for regression](https://missinglink.ai/guides/neural-network-concepts/neural-networks-regression-part-1-overkill-opportunity/)  
[random forest regression](https://www.geeksforgeeks.org/random-forest-regression-in-python/)   
[multivariate forecasting with LSTM Keras](https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/)  
[time series forecasting with LSTM](https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/)   
[multi-step forecasting with LSTM](https://machinelearningmastery.com/multi-step-time-series-forecasting-long-short-term-memory-networks-python/)   
[tuning hyper parameters of estimators](https://scikit-learn.org/stable/modules/grid_search.html)  
[BTC LSTM Prediction](http://www.quantatrisk.com/2020/04/01/how-to-predict-bitcoin-price-deep-learning-lstm-network-python/#:~:text=Design%20and%20train%20the%20LSTM,the%20entire%20test%20data%20sample.)  
[Weight regularization with lstm forecasting](https://machinelearningmastery.com/use-weight-regularization-lstm-networks-time-series-forecasting/)   
[Tune LSTM Hyperparamets with Keras for Forescasting](https://machinelearningmastery.com/tune-lstm-hyperparameters-keras-time-series-forecasting/)  
[Different Batch Sizes whe training and predicting with lstms](https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/)  

https://www.analyticsvidhya.com/blog/2020/02/cnn-vs-rnn-vs-mlp-analyzing-3-types-of-neural-networks-in-deep-learning/



### Quantitative/algorithmic Trading Resources
---
[shrimpy github](https://github.com/shrimpy-dev/shrimpy-python)  
[shrimpy developer](https://developers.shrimpy.io/docs/?python#rebalancing) 
[shrimpy](https://www.shrimpy.io/)  
[shrimpy x coinbase](https://blog.shrimpy.io/blog/python-scripts-for-coinbase-pro-market-data)  
[shrimpy trading bot](https://blog.shrimpy.io/blog/how-to-make-a-crypto-trading-bot-using-python)  
[shrimpy api](https://blog.shrimpy.io/blog/how-to-make-a-crypto-trading-bot-using-python)  
https://blog.shrimpy.io/blog/free-universal-websockets-for-real-time-crypto-exchange-order-book-data

https://blog.shrimpy.io/blog/free-historical-ohlcv-trade-charting-data-for-crypto-exchanges

[Smart Order Routing: Shrimpy](https://blog.shrimpy.io/blog/crypto-api-for-smart-order-routing)  
https://blog.shrimpy.io/blog/historical-crypto-exchange-order-book-snapshots


[Threshold Rebalancing: Evolution of Crypto Portfolio Management](https://blog.shrimpy.io/blog/threshold-rebalancing-the-evolution-of-cryptocurrency-portfolio-management)  
[Guide To Crypto Currency Trading Bots](https://blog.shrimpy.io/blog/cryptocurrency-trading-bots-the-complete-guide)  
[Rebalance Frequency Analysis](https://blog.shrimpy.io/blog/an-analysis-of-high-frequency-rebalancing)   
[CRYPTO PORTFOLIO DIVERSITY STUDY: More Assets equal greater returns](https://hackernoon.com/portfolio-diversity-a-technical-analysis-c2c49f4d3a77)  
[Best Threshold Rebalance](https://blog.shrimpy.io/blog/the-best-threshold-for-cryptocurrency-rebalancing-strategies)  
[LIQUIDITY STUDY: ALL FACTORS MATTER](https://blog.goodaudience.com/exchange-liquidity-a-comparative-study-e184ef7162f)  
[Machine Learning Options for CryptoCurrency Price Prediction]
[Shrimpy WhitePaper](https://www.shrimpy.io/shrimpy-whitepaper.pdf)  
[BTC ACUMMULATION](https://blog.shrimpy.io/blog/taking-profit-crypto-portfolio-strategies)
[SHRIMPY APP trades over 1 Billion](https://medium.com/the-innovation/how-our-crypto-app-traded-over-1-billion-b2a96217d91e)  
[ML for CRYPTO PORTFOLIO MANAGMENT](https://blog.shrimpy.io/blog/machine-learning-for-crypto-portfolio-management-case-study-week-20)  
[RESEARCH- Diversification Benefits](https://research.binance.com/en/analysis/bitcoin-diversification-benefits)    
[RESEARCH- Cluster Analysis](https://research.binance.com/en/analysis/cluster-analysis)  




[alphalens](https://www.quantopian.com/docs/api-reference/alphalens-api-reference#alphalens.utils.get_clean_factor_and_forward_returns) 
[blueshift](https://blueshift.quantinsti.com/research/strategies/3a32abeec97fa9cd5b7ee4f038d208d8/edit) 
[kraken](https://www.kraken.com/)  
[bittrex](https://bittrex.com)  
[coinbase pro](https://pro.coinbase.com/)  
[3 line backtest](https://towardsdatascience.com/backtest-your-trading-strategy-with-only-3-lines-of-python-3859b4a4ab44)  

[trading view](https://www.tradingview.com/chart/ZCmPZo4J/)  

https://hub.docker.com/r/probcomp/mit-6.885-spring2019-pset-1-student
https://hub.docker.com/r/probcomp/mit-6.885-spring2019-pset-2-student


### Crypto Research Resources
---
[cryptocompare](https://www.cryptocompare.com/)  
[s2f](https://medium.com/@100trillionUSD/modeling-bitcoins-value-with-scarcity-91fa0fc03e25)  
[heart capital research](https://github.com/gdepalma93/heartcap/blob/master/Market_Research.ipynb)  

### GITLAB 
https://about.gitlab.com/solutions/agile-delivery/
https://www.youtube.com/watch?v=VR2r1TJCDew
https://plan.io/blog/sprint-planning/



### DATA PROVIDERS
- https://blog.shrimpy.io/blog/the-best-apis-for-cryptocurrency-historical-data
- https://www.kaiko.com/pages/historical-data  
- https://cryptowat.ch/
- https://docs.coinapi.io/#historical-data-2
- https://www.alphavantage.co/documentation/
- https://www.cryptodatadownload.com/data/binance/
- https://www.coinigy.com/bitcoin-data/

### 
- https://www.cryptodatadownload.com/analytics/var/



### Story Arc
    - Phase 1
        - NU FINTECH BOOTCAMP
        - Qauntopian System: Project 1
        - Project Mantis: Project 2
        - Mantis Trading: Project 3
            - minimal viable product
    - Phase 2:
        - Productionalize Crypto Trading System
    - Phase 3:
        - 