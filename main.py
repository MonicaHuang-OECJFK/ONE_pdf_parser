from ONE_parser import parse_one_pdf
from export_excel import export_to_excel

data = parse_one_pdf("test.pdf")

# 👉 原本 debug（可以保留）
for i, block in enumerate(data):
    print("\n====================")
    print(f"BLOCK {i}")
    print("COMMODITY:", block["commodity_label"])
    print("PAGES:", f'{block["start_page"]} -> {block["end_page"]}')
    print("VALID TO:", block["valid_to"])

    for origin in block["origins"]:
        print("  ORIGIN:", origin["origin"])
        print("  COUNT:", len(origin["rates"]))
        print("  SAMPLE:", origin["rates"][:2])

# 👉 ⭐ 新增這行（關鍵）
export_to_excel(data, "ONE_output.xlsx")

print("\n✅ Excel generated: ONE_output.xlsx")