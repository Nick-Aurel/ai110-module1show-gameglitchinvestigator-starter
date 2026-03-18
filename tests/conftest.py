from __future__ import annotations

import sys
from pathlib import Path

# Ensure the repo root (which contains logic_utils.py) is importable when pytest
# runs from environments that don't automatically add it to sys.path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

