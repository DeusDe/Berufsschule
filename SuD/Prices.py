prices = {
    'adult' : 10,
    'kid' : 5,
    'teen' : 6,
    'premium' : 6,
    'basic' : 5,
}

#Für die generation der halben Preise
for key in prices.copy():
    prices[str(key) + '_half'] = prices[key] / 2