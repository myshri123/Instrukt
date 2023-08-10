"""Devtools and utils for debugging"""

import logging
import os
import subprocess
from typing import TYPE_CHECKING

from xdg import BaseDirectory
from ..config import APP_SETTINGS

if TYPE_CHECKING:
    from debugpy import Endpoint

dap_conn = None
DAP_PORT = 5678

#DEBUG: used for debugging purposes only
if APP_SETTINGS.debug:

    def notify(msg: str) -> None:
        pass
        # call a system command `dunstify` to send`
        # subprocess.call(['dunstify', '-u', 'critical', msg])
    import debugpy
    dap_conn  = debugpy.listen(DAP_PORT)
    # debugpy.wait_for_client()
else:
    def notify(msg: str) -> None:
        pass


def get_dbg_path() -> str:
    """Returns the debug path"""
    return BaseDirectory.save_cache_path("instrukt")


def log_llm_output(msg: str) -> None:
    """Logs the msg to the file"""
    debug_path = BaseDirectory.save_cache_path("instrukt")
    debug_file = os.path.join(debug_path, "debug_llm_output.log")
    with open(debug_file, "a") as f:
        f.write(msg + "\n")


def dbg_file_logger() -> None:
    """Returns a file based logger"""
    debug_path = BaseDirectory.save_cache_path("instrukt")
    debug_file = os.path.join(debug_path, "debug.log")
    logger = logging.getLogger("instrukt_dbg_file")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(debug_file)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
