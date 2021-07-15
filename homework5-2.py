with open("text-1.txt", "r", encoding="utf-8") as f:
    for line, count in enumerate(f, 1):
        print(f'{line}. {"".strip()} - {len(count.split())} words')
    f.seek(0)
    print(f"{sum(1 for _ in f)} lines")
