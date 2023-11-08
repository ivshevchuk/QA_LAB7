import paramiko
import subprocess
import pytest
import sys


server_ip = "192.168.56.101"
port = 22


@pytest.fixture(scope="function")
def server():
    sshClient = paramiko.SSHClient()
    try:
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.connect(hostname=server_ip, port=port)
        stdin, stdout, stderr = sshClient.exec_command("iperf3 -s -1")
        stdin.close()
    except paramiko.AuthenticationException:
        sys.exit(1)
    finally:
        sshClient.close()


@pytest.fixture(scope="function")
def client():
    return subprocess.run(["iperf3", "-c", server_ip, "--json"], capture_output=True, text=True)
