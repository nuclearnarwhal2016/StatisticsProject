import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.read_csv('AmesHousing.csv')

price_samp = df.sample(n=500, replace=False)

num_iterations = 10000

df_medians = []
for _ in range(num_iterations):
    resample = np.random.choice(price_samp['SalePrice'], size=30, replace=True)
    df_medians.append(np.median(resample))

fig, axs = plt.subplots(1, 3, figsize=(10, 8))
axs[0].hist(df_medians, bins=30, density=True,
            color='skyblue', edgecolor='black')
axs[0].set_title('Median histogram')
axs[0].set_xlabel("Prices")
axs[0].set_ylabel("Proportion")

axs[1].hist(df['SalePrice'], bins=30, density=True,
            color='skyblue', edgecolor='black')
axs[1].set_title('Population histogram')
axs[1].set_xlabel("Prices")
axs[1].set_ylabel("Proportion")

axs[2].hist(price_samp['SalePrice'], bins=10, density=True,
            color='skyblue', edgecolor='black')
axs[2].set_title('Sample histogram')
axs[2].set_xlabel("Prices")
axs[2].set_ylabel("Proportion")

summary_table = pd.DataFrame({'Iteration': range(1, num_iterations+1),
                              'Median': df_medians})
print(summary_table)

plt.tight_layout()
plt.show()
