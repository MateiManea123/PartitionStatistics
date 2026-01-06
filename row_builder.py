
ROUND_DECIMALS = 2

def build_rows(stats: dict, total_files: int):
    total_size = sum(v[1] for v in stats.values())

    rows = []
    for ext, (count, size) in stats.items():
        count_pct = (count / total_files) * 100 if total_files else 0
        size_pct = (size / total_size) * 100 if total_size else 0

        rows.append({
            "ext": ext,
            "count": count,
            "size": size,
            "count_pct": round(count_pct, ROUND_DECIMALS),
            "size_pct": round(size_pct, ROUND_DECIMALS),
        })

    return rows, total_size

def top_with_other(rows, key_name: str, top_n: int):
    rows_sorted = sorted(rows, key=lambda r: r[key_name], reverse=True)
    main = rows_sorted[:top_n]
    rest = rows_sorted[top_n:]

    if rest:
        other = {
            "ext": "Other",
            "count": sum(r["count"] for r in rest),
            "size": sum(r["size"] for r in rest),
            "count_pct": round(sum(r["count_pct"] for r in rest), ROUND_DECIMALS),
            "size_pct": round(sum(r["size_pct"] for r in rest), ROUND_DECIMALS),
        }
        main.append(other)

    return main

def print_phase2_table(rows, title: str):
    print(f"\n--- {title} ---")
    print("Extension | Count % | Size % | Count | Size (bytes)")
    print("-" * 60)
    for r in rows:
        print(
            f"{r['ext']:>9} | "
            f"{r['count_pct']:>7.2f}% | "
            f"{r['size_pct']:>6.2f}% | "
            f"{r['count']:>5} | "
            f"{r['size']}"
        )