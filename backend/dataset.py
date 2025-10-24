import pandas as pd
import numpy as np

np.random.seed(42)

data_size = 400
area = np.random.randint(600, 4000, data_size)
bedrooms = np.random.randint(1, 6, data_size)
age = np.random.randint(0, 30, data_size)
locations = np.random.choice(['City Center', 'Suburb', 'Village'], data_size)

price = (area * 5000) + (bedrooms * 200000) - (age * 15000)
price += np.where(locations == 'City Center', 1000000, 0)
price += np.random.randint(-200000, 200000, data_size)

df = pd.DataFrame({
    'Area': area,
    'Bedrooms': bedrooms,
    'Age': age,
    'Location': locations,
    'Price': price
})

df.to_csv("house_data.csv", index=False)
print("Dataset created successfully ✅")
