import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="gofumpt",
    cmd="gofumpt",
    repo_name="mvdan/gofumpt",
    filename_template="gofumpt_{version}_{platform}_{arch}",
    arch_map={
        "x86_64": "amd64",
        "aarch64": "arm64",
    },
    checksum_filename_template="sha256sums.txt",
    bin_path="gofumpt",
    recover_raw_version=lambda x: f"v{x}",
    is_compressed=False,
)
