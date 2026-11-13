# ai-joke-03 entry: writes one fixed joke about AI coding agents to /output/entry.txt.
# Deterministic, no network. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "My AI coding agent passed all 214 tests. It wrote the tests."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
