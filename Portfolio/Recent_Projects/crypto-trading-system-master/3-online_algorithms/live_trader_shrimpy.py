# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:43:44 2020

@author: GrantDePalma
"""
#----------- Data Prep -------------------

# Import shrimpy websocket connections
#   Balance Stream
#   Trade Stream
#   Account Stream
#   Stream shrimpy specific channels: bbo(best bid offer), orderbook, trade, orders 



# Import libraries and dependencies
import shrimpy
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

exchanges= ['kraken', 'kucoin', 'bittrex', 'coinbase_pro', 'binance', 'gemini']
strategies = ['btc_accumulator', 'wave_rider', 'master_quant']
# BTC Accumulator
    # 6hr rebalance, threshold rebalance to 

# Set environment variables from the .env file
env_path = Path("/Users/GrantDePalma")/'.env'
load_dotenv(env_path)

shrimpy_public_key = os.getenv("SHRIMPY_PUBLIC_KEY")
shrimpy_private_key = os.getenv("SHRIMPY_PRIVATE_KEY")
exchange_name = 'kraken'
exchange_public_key = os.getenv("exchange_public_key")
exchange_secret_key = os.getenv("exchange_secret_key")

client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_private_key)

# Set User ID
users = client.list_users()
user_id = users[0]['id'] # first id in list of users

# Exchange Data
exchange_public_key = exchange_public_key
exchange_secret_key = exchange_secret_key

# Link kraken exchange 
link_account_response = client.link_account(user_id,
                                           exchange_name,
                                           exchange_public_key,
                                           exchange_secret_key)
account_id = link_account_response['id']

balance = client.get_balance(user_id, account_id)
holdings = balance['balances']
for asset in holdings:
    asset_symbol = asset['symbol']
    asset_amount = asset['nativeValue']
    print(asset_symbol + ' ' + str(asset_amount) )
    
    
    
    
    ---------- Generate Signal Dataframes -----------
    # btc_ccumulator- Threshold Rebalance into BTC
    # wave_rider-ema_crosses
    # calculus_index- continuous quant strategies
    # 



    -------  
    

