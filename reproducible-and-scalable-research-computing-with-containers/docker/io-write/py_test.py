import sys,os

import pandas as pd



args = sys.argv

input = args[1]

output = args[2]+"output.csv"



df = pd.read_csv(input)

print(df)



data = { 'Company' : ['VW','Toyota','Renault','KIA','Tesla'], 'Cars Sold (millions)' : [10.8,10.7,10.3,7.4,0.25], 'Best Selling Model' : ['Golf','RAV4','Clio','Forte','Model 3']}

frame = pd.DataFrame(data)

# Thanks to Chen Chen for suggesting the following 2 lines to avoid partail failure of the image run.
if not os.path.exists(args[2]):
    os.makedirs(args[2])

frame.to_csv(output)

print("This is a Python test in docker!")
