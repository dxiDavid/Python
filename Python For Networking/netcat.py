import socket
import subprocess
import sys
import threading
import argparse
import textwrap
import shlex


def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    # return output.decode()
    print(output.decode())

execute("  ")
