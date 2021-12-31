import subprocess
import os
from pathlib import Path


def get_secrets():
    home = os.path.expanduser(
        os.path.join(
            os.environ.get('PASSWORD_STORE_DIR', '~/.password-store'), ''
        )
    )
    file_extention = ".gpg"

    for secret in Path(home).rglob("*"+file_extention):
        secret_name = secret.as_posix().replace(
            home, "").replace(file_extention, "")
        yield secret_name


def get_secret(secret_name):
    return subprocess.check_output(["pass", secret_name])
