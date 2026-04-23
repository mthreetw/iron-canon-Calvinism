from pathlib import Path

root = Path(".")
order = [
    "提綱","卷1 存在論", "卷2 神論", "卷3 人論", "卷4 啟示論",
    "卷5 救贖論", "卷6 爭戰", "卷7 教會論", "卷8 末世論", "卷9 當代回應"
]

with open("iron-canon-complete.md", "w", encoding="utf-8") as out:
    for folder in order:
        p = root / folder
        if not p.exists():
            print(f"找不到資料夾：{folder}")
            continue
        files = sorted(p.glob("卷*.md"))
        if not files:
            print(f"沒有找到主文件：{folder}")
            continue
        for md in files:
            print(f"合併：{md}")
            out.write(md.read_text(encoding="utf-8"))
            out.write("\n\n---\n\n")

print("完成：iron-canon-complete.md")