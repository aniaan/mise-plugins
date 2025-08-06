import subprocess
import sys
import tempfile
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import FormatKwargs, Plugin, extract

_CMD = "minisign"
_PUBLIC_KEY = "RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3"


def _filename_template(kwargs: FormatKwargs):
    suffix = "zip"
    if kwargs["platform"] == "linux":
        suffix = "tar.gz"

    return f"minisign-{kwargs['version']}-{kwargs['platform']}.{suffix}"


def _checker(file_path: Path, checksum_path: Path, format_kwargs: FormatKwargs):
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        extract_path = tmp_path / "extract"
        extract_path.mkdir(exist_ok=True)

        extract(download_path=file_path, extract_path=extract_path, bin_path=_CMD)

        if format_kwargs["platform"] == "linux":
            bin_path = (
                extract_path / "minisign-linux" / format_kwargs["arch"] / "minisign"
            )
        else:
            bin_path = extract_path / "minisign"

        bin_path.chmod(0o755)

        # call process: bin_path -P PUBLIC_KEY -x checksum_path -Vm file_path
        cmd = [bin_path, "-P", _PUBLIC_KEY, "-x", checksum_path, "-Vm", file_path]
        result = subprocess.run([*cmd, file_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error checking signature: {result.stderr}")


def _bin_path_template(kwargs: FormatKwargs):
    if kwargs["platform"] == "linux":
        bin_path = f"minisign-linux/{kwargs['arch']}/minisign"
    else:
        bin_path = "minisign"

    return bin_path


PLUGIN = Plugin(
    name="minisign",
    cmd=_CMD,
    repo_name="jedisct1/minisign",
    filename_template=_filename_template,
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    bin_path=_bin_path_template,
    checksum_filename_template="{filename}.minisig",
    custom_checker=_checker,
)
