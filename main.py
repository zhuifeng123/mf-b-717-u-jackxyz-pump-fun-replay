import os

output_dir = "/output"
entry_file = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

entry_text = "PaperBot leads the Pump.fun replay sprint: deterministic, lean, real ranking, no fluff, pure edge."

with open(entry_file, "w") as f:
    f.write(entry_text + "\n")