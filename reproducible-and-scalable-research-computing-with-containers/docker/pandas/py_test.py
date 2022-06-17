import pandas as pd

data = { 'Company' : ['VW','Toyota','Renault','KIA','Tesla'], 'Cars Sold (millions)' : [10.8,10.7,10.3,7.4,0.25], 'Best Selling Model' : ['Golf','RAV4','Clio','Forte','Model 3']}

frame = pd.DataFrame(data)

frame.info()

print("This is a Python test in docker!")
