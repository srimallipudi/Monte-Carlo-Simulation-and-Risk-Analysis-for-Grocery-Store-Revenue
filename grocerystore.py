#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:01:01 2024

@author: srilu
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(1)

# Number of simulations
num_simulations = 1000

# Customer statistics
num_customers = 220
baked_goods_prob = 0.3
meat_dairy_prob = 0.7
produce_prob = 0.8
frozen_food_prob = 0.65

# Fresh baked goods (uniform distribution)
baked_goods = np.random.uniform(3, 19, size=(num_simulations, num_customers)) * (np.random.rand(num_simulations, num_customers) < baked_goods_prob)

# Meat and dairy (normal distribution)
meat_dairy = np.random.normal(21, 5.27, size=(num_simulations, num_customers)) * (np.random.rand(num_simulations, num_customers) < meat_dairy_prob)

# Produce (normal distribution)
produce = np.random.normal(15, 2.31, size=(num_simulations, num_customers)) * (np.random.rand(num_simulations, num_customers) < produce_prob)

# Frozen food (uniform distribution)
frozen_food = np.random.uniform(7.25, 28.50, size=(num_simulations, num_customers)) * (np.random.rand(num_simulations, num_customers) < frozen_food_prob)

# Calculate total spending for each customer
total_spending = baked_goods + meat_dairy + produce + frozen_food

# Calculate daily revenue
daily_revenue = np.sum(total_spending, axis=1)

# Analyze results
average_daily_revenue = np.mean(daily_revenue)
std_dev_daily_revenue = np.std(daily_revenue)
max_daily_revenue = np.max(daily_revenue)
min_daily_revenue = np.min(daily_revenue)

print("Average Daily Revenue: ${:.2f}".format(average_daily_revenue))
print("Standard Deviation of Daily Revenue: ${:.2f}".format(std_dev_daily_revenue))
print("Maximum Daily Revenue: ${:.2f}".format(max_daily_revenue))
print("Minimum Daily Revenue: ${:.2f}".format(min_daily_revenue))