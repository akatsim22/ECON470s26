# unzip enrollment files
import zipfile
from pathlib import Path

zip_dir = Path("data/input/enrollment2018")
out_dir = zip_dir / "csv"

out_dir.mkdir(exist_ok=True)

for zip_path in zip_dir.glob("*.zip"):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(out_dir)

print("Enrollment CSVs extracted.")

# unzip service area files
import zipfile
from pathlib import Path

zip_dir = Path("data/input/service_area2018")
out_dir = zip_dir / "csv"

out_dir.mkdir(exist_ok=True)

for zip_path in zip_dir.glob("*.zip"):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(out_dir)

print("Service area CSVs extracted.")