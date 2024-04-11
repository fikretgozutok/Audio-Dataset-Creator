import pandas as pd

# Örnek bir DataFrame oluşturalım
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)

print("DataFrame Öncesi:")
print(df)

# 2. satırı (indeksleme 0'dan başladığı için 1. satır) silelim
df = df.drop(1)

print("\nDataFrame Sonrası:")
print(df)
