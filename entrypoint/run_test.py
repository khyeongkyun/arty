from src.graphs.main_graph import build_graph
from pathlib import Path

graph = build_graph()

state = graph.invoke(
    {"topic": "How does the private Art curator work? Keep it concise and easy to understand for everyone."}
)

final_report = state["final_report"]

# Define output path
output_file = Path("final_report.md")

# Write the Markdown content
with output_file.open("w", encoding="utf-8") as f:
    f.write(final_report)

print(f"Report saved to {output_file.resolve()}")