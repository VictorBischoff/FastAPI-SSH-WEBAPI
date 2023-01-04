"""Perform tasks against a remote host."""
from typing import List

from config import (
    SSH_KEY_FILEPATH,
    SSH_PASSWORD,
    SSH_REMOTE_HOST,
    SSH_USERNAME,
)
from ssh.model_BU import RemoteClient
from .model_BU import RemoteClient


def run():
    """Initialize remote host client and execute actions."""
    client = RemoteClient(
        SSH_REMOTE_HOST,
        SSH_USERNAME,
        SSH_PASSWORD,
        SSH_KEY_FILEPATH,
    )
    execute_command_on_remote(
        client,
        [
            "mkdir uploadsTest",
            "cd uploadsTest/ && ls",
        ],
    )

def execute_command_on_remote(client: RemoteClient, commands: List[str]):
    """
    Execute a UNIX command remotely on a given host.
    :param RemoteClient client: Remote server client.
    :param List[str] commands: List of commands to run on remote host.
    """
    client.execute_commands(commands)