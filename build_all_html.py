import pandas as pd
import os

excel_file = "★마곡아이파크 디어반 견적서(전체호실)_할인분양가적용(20251104).xlsx"
xl = pd.ExcelFile(excel_file)

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>남은호실 방문 전용 전체 엑셀 현황</title>
    <!-- Bootstrap for tabs and tables -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/variable/pretendardvariable.css" />
    <style>
        body { font-family: 'Pretendard Variable', sans-serif; background-color: #f8fafc; padding: 20px; }
        .wrapper { background: #fff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .table-responsive { max-height: 700px; overflow-y: auto; }
        table { font-size: 0.85rem; white-space: nowrap; }
        th { position: sticky; top: 0; background-color: #e2e8f0 !important; color: #1e293b; }
        .nav-tabs .nav-link { font-weight: bold; color: #64748b; }
        .nav-tabs .nav-link.active { color: #0f172a; border-bottom: 3px solid #6366f1; }
        .btn-back { display: inline-block; margin-bottom: 20px; text-decoration: none; background: #1e293b; color: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 600; }
        .btn-back:hover { background: #0f172a; color: #fff; }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="mb-0 fw-bold" style="color:#1e293b;">🏢 남은호실 전체 리스트 (엑셀 원본 데이터)</h2>
            <a href="index.html" class="btn-back">← 메인 홈페이지로 돌아가기</a>
        </div>
        
        <ul class="nav nav-tabs" id="myTab" role="tablist">
"""

tab_contents = """<div class="tab-content mt-3" id="myTabContent">"""

for i, sheet_name in enumerate(xl.sheet_names):
    # Skip completely empty columns/rows if possible, but keep structure
    df = xl.parse(sheet_name)
    df.dropna(how='all', inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    
    # HTML clean table
    table_html = df.to_html(classes="table table-bordered table-hover tabulator", index=False, na_rep="")
    
    active = "active" if i == 0 else ""
    aria_selected = "true" if i == 0 else "false"
    
    html_content += f"""
            <li class="nav-item" role="presentation">
                <button class="nav-link {active}" id="tab-{i}" data-bs-toggle="tab" data-bs-target="#content-{i}" type="button" role="tab" aria-selected="{aria_selected}">{sheet_name}</button>
            </li>
    """
    
    show_active = "show active" if i == 0 else ""
    tab_contents += f"""
            <div class="tab-pane fade {show_active}" id="content-{i}" role="tabpanel">
                <div class="table-responsive border rounded">
                    {table_html}
                </div>
            </div>
    """

html_content += """
        </ul>
"""
html_content += tab_contents
html_content += """
        </div>
    </div>
    
    <!-- Bootstrap JS for Tabs -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

with open('status_excel.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
