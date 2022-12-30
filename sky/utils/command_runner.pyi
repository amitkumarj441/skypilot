import enum
import typing
from _typeshed import Incomplete
from sky import sky_logging as sky_logging
from sky.skylet import log_lib as log_lib
from sky.utils import subprocess_utils as subprocess_utils
from typing import List, Optional, Tuple, Union
from typing_extensions import Literal

GIT_EXCLUDE: str
RSYNC_DISPLAY_OPTION: str
RSYNC_FILTER_OPTION: str
RSYNC_EXCLUDE_OPTION: str


def ssh_options_list(ssh_private_key: Optional[str],
                     ssh_control_name: Optional[str],
                     *,
                     timeout: int = ...) -> List[str]:
    ...


class SshMode(enum.Enum):
    NON_INTERACTIVE: int
    INTERACTIVE: int
    LOGIN: int


class SSHCommandRunner:
    ip: str
    ssh_user: str
    ssh_private_key: str
    ssh_control_name: Optional[str]

    def __init__(self,
                 ip: str,
                 ssh_user: str,
                 ssh_private_key: str,
                 ssh_control_name: Optional[str] = ...) -> None:
        ...

    @staticmethod
    def make_runner_list(
            ip_list: List[str],
            ssh_user: str,
            ssh_private_key: str,
            ssh_control_name: Optional[str] = ...) -> List['SSHCommandRunner']:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[False] = ...,
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            **kwargs) -> int:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[True],
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            **kwargs) -> Tuple[int, str, str]:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: bool = ...,
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            **kwargs) -> Union[Tuple[int, str, str], int]:
        ...

    def rsync(self,
              source: str,
              target: str,
              *,
              up: bool,
              log_path: str = ...,
              stream_logs: bool = ...) -> None:
        ...
