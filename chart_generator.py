import os
import matplotlib.pyplot as plt

CHART_DIR = "charts"
TOP_N = 10

def ensure_chart_dir():
    if not os.path.exists(CHART_DIR):
        os.makedirs(CHART_DIR)

def pie_chart(labels, values, title, filename):
    plt.figure(figsize=(10, 6))

    def autopct(pct):
        return f"{pct:.2f}%" if pct >= 1 else ""

    wedges, _, _ = plt.pie(
        values,
        labels=None,
        autopct=autopct,
        startangle=90
    )

    plt.title(title)
    plt.axis("equal")

    plt.legend(
        wedges, labels,
        title="File types",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5)
    )

    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, filename), dpi=200)
    plt.show()

def bar_chart(labels, values, title, ylabel, filename, log_scale=False):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")

    if log_scale:
        plt.yscale("log")

    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, filename), dpi=200)
    plt.show()

def generate_charts(data_by_count, data_by_size):
    ensure_chart_dir()

    labels_c = [r["ext"] for r in data_by_count]
    counts = [r["count"] for r in data_by_count]

    pie_chart(labels_c, counts,
              "File Type Distribution by Count",
              "pie_count.png")

    bar_chart(labels_c, counts,
              f"Top {TOP_N} File Types by Count (+Other)",
              "File Count",
              "bar_count.png",
              log_scale=False)

    labels_s = [r["ext"] for r in data_by_size]
    sizes = [r["size"] for r in data_by_size]

    pie_chart(labels_s, sizes,
              "File Type Distribution by Total Size",
              "pie_size.png")

    bar_chart(labels_s, sizes,
              f"Top {TOP_N} File Types by Total Size (+Other)",
              "Total Size (bytes)",
              "bar_size.png",
              log_scale=True)
