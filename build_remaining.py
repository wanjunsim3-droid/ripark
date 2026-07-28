import pandas as pd
import json
import math

df = pd.read_excel('임대용(24.05.27)_★마곡아이파크 디어반 견적서(계좌번호) 240527 (1) (1).xlsx')
data = []

# Using heuristics to find rows with data
for i, r in df.iterrows():
    unit = str(r.iloc[0]).strip()
    # It must be a valid unit number usually digits or b-digit
    if pd.isna(r.iloc[0]) or unit == 'nan' or unit == '' or '호' in unit or '합계' in unit:
        continue
    
    try:
        # Checking if the unit looks like a valid number or floor identifier (like 101, B101, etc)
        # We assume if Unnamed: 2 and Unnamed: 4 and Unnamed: 9 are valid numbers, it's a room row
        if pd.isna(r.iloc[2]) or pd.isna(r.iloc[4]) or pd.isna(r.iloc[9]):
            continue
            
        j_py = round(float(r.iloc[2]), 2)
        g_py = round(float(r.iloc[4]), 2)
        price = int(r.iloc[9])
        
        if j_py > 0:
            data.append({
                'unit': unit,
                'j_py': j_py,
                'g_py': g_py,
                'price': price
            })
    except Exception as e:
        continue

with open('data_remaining.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print(f"Extracted {len(data)} units.")
