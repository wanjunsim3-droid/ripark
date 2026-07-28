import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>호실별 평수 및 분양가 현황판</title>
    <!-- Tabulator CSS -->
    <link href="https://unpkg.com/tabulator-tables@5.5.0/dist/css/tabulator_bootstrap5.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/variable/pretendardvariable.css" />
    <style>
        body {{ font-family: 'Pretendard Variable', sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; }}
        .wrapper {{ max-width: 1200px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); }}
        h1 {{ color: #1a2233; margin-bottom: 20px; font-weight: 800; border-left: 5px solid #d1122a; padding-left: 15px; }}
        .top-actions {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px; }}
        .btn-back {{ text-decoration: none; background: #1a2233; color: #fff; padding: 10px 20px; border-radius: 8px; font-weight: bold; transition: 0.3s; }}
        .btn-back:hover {{ background: #0f172a; }}
        
        /* Excel Table Customization */
        .tabulator {{ font-size: 14px; border: none !important; }}
        .tabulator-header {{ background-color: #f8fafc !important; color: #1e293b; font-weight: bold; }}
        .tabulator-col-title {{ text-align: center; }}
        .tabulator-row {{ border-bottom: 1px solid #e2e8f0; }}
        .tabulator-row:nth-child(even) {{ background-color: #f8fafc; }}
        .tabulator-cell {{ text-align: right; padding: 12px !important; }}
        .tabulator-cell:first-child {{ text-align: center; font-weight: bold; color: #1a2233; }}
        .tabulator-footer {{ background-color: #e2e8f0 !important; font-weight: bold; }}
        
        .summary-cards {{ display: flex; gap: 15px; margin-bottom: 20px; }}
        .summary-card {{ flex: 1; background: #fff; border: 1px solid #e2e8f0; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border-left: 4px solid #6366f1; }}
        .summary-card h3 {{ margin: 0 0 10px 0; font-size: 14px; color: #64748b; }}
        .summary-card p {{ margin: 0; font-size: 24px; font-weight: 800; color: #1e293b; }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="top-actions">
            <h1>📊 마곡 아이파크 디어반 호실별 상세 테이블</h1>
            <a href="index.html" class="btn-back"><i class="fa-solid fa-arrow-left"></i> 메인으로 돌아가기</a>
        </div>
        
        <div class="summary-cards">
            <div class="summary-card" style="border-left-color: #3b82f6;">
                <h3>총 전용면적(평) 합계</h3>
                <p id="sumJpy">계산중...</p>
            </div>
            <div class="summary-card" style="border-left-color: #10b981;">
                <h3>총 계약면적(평) 합계</h3>
                <p id="sumGpy">계산중...</p>
            </div>
            <div class="summary-card" style="border-left-color: #ef4444;">
                <h3>총 분양가 합계(원)</h3>
                <p id="sumPrice">계산중...</p>
            </div>
        </div>

        <div id="excel-table"></div>
    </div>
    
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@5.5.0/dist/js/tabulator.min.js"></script>
    <script>
        // Data injected from Python
        const tableData = {json.dumps(data)};
        
        // Calculate Totals Header
        let tJpy = 0, tGpy = 0, tPrice = 0;
        tableData.forEach(row => {{
            tJpy += row.j_py;
            tGpy += row.g_py;
            tPrice += row.price;
        }});
        
        document.getElementById('sumJpy').innerText = tJpy.toFixed(2) + " 평";
        document.getElementById('sumGpy').innerText = tGpy.toFixed(2) + " 평";
        document.getElementById('sumPrice').innerText = tPrice.toLocaleString() + " 원";

        // Initialize Tabulator
        var table = new Tabulator("#excel-table", {{
            data: tableData,
            layout: "fitColumns",
            responsiveLayout: "collapse",
            pagination: "local",
            paginationSize: 50,
            columnDefaults: {{ tooltip: true }},
            columns: [
                {{title: "호실 번호 (검색)", field: "unit", headerFilter: "input", frozen: true, width: 200}},
                {{title: "전용면적 (평)", field: "j_py", bottomCalc: "sum", bottomCalcParams: {{precision: 2}}}},
                {{title: "계약면적 (평)", field: "g_py", bottomCalc: "sum", bottomCalcParams: {{precision: 2}}}},
                {{title: "할인 잔금분양가 (원)", field: "price", formatter: "money", formatterParams: {{precision: false, symbol:"₩"}}, bottomCalc: "sum", bottomCalcFormatter: "money", bottomCalcFormatterParams: {{precision: false, symbol:"₩"}}}}
            ],
            locale: true,
        }});
    </script>
</body>
</html>"""

with open('status_excel.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
