import pandas as pd
import json

df = pd.read_excel('★마곡아이파크 디어반 견적서(전체호실)_할인분양가적용(20251104).xlsx')
data = []

for i, r in df.iloc[13:].iterrows():
    unit = str(r.iloc[1]).strip()
    if pd.isna(r.iloc[1]) or unit == 'nan' or '합계' in unit or '소계' in unit or unit == '':
        continue
    
    try:
        j_py = round(float(r.iloc[4]), 2) if not pd.isna(r.iloc[4]) else 0.0
        g_py = round(float(r.iloc[6]), 2) if not pd.isna(r.iloc[6]) else 0.0
        price = int(r.iloc[15]) if not pd.isna(r.iloc[15]) else 0
        if j_py > 0:
            data.append({
                'unit': unit,
                'j_py': j_py,
                'g_py': g_py,
                'price': price
            })
    except Exception as e:
        continue

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
