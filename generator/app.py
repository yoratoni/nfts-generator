from core import GeneralPaths

import os

path = os.path.join(os.getcwd(), "assets", "input", "elon")

print(GeneralPaths.scan_structure(path))