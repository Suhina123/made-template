#Step 1 : Download the CSV file
import urllib.request
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
response = urllib.request.urlopen(url)
csv_data = response.read().decode('utf-8')

# Step 2: Reading the CSV file into a pandas DataFrame
df = pd.read_csv(StringIO(csv_data),sep=';')

# Step 3: Define the SQLite database connection and create an SQLAlchemy engine
db_connection_str = 'sqlite:///airports.sqlite'
engine = create_engine(db_connection_str)

# Step 4: Write the DataFrame to the SQLite database
df.to_sql('airports', con=engine, index=False, if_exists='replace')



# Close the engine
engine.dispose()