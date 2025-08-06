import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="hadolint",
    cmd="hadolint",
    repo_name="hadolint/hadolint",
    filename_template="hadolint-{platform}-{arch}",
    platform_map={
        "darwin": "Darwin",
        "linux": "Linux",
    },
    arch_map={
        "x86_64": "x86_64",
        "aarch64": "arm64",
    },
    checksum_filename_template="{filename}.sha256",
    bin_path="hadolint",
    recover_raw_version=lambda x: f"v{x}",
    is_compressed=False,
)
