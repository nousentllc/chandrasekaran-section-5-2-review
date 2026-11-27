"""Run the numerical and symbolic checks in an isolated working directory."""

from pathlib import Path
import subprocess
import sys
import tempfile

FILES = ("operator_checks.py", "countermodel.py", "section5-3_coefficient_identity.py",
         "verify_v1_2_f5.py", "check_gaussian_band.py", "check_center_moments.py",
         "check_fourier_blocks.py")


def main():
    root = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as scratch:
        Path(scratch, "outputs").mkdir()
        for name in FILES:
            run = subprocess.run([sys.executable, str(root / name)], cwd=scratch,
                                 check=True, stdout=subprocess.PIPE)
            print(name, flush=True)
            print(run.stdout.decode().rstrip(), flush=True)
            if name == "verify_v1_2_f5.py":
                if run.stdout != (root / "reference/verify_v1_2_f5.log").read_bytes():
                    print("Printed floating-point output differs from the archived log.")
        for name in ("operator_checks.json", "countermodel_checks.json"):
            current = Path(scratch, "outputs", name).read_bytes()
            archived = (root / "reference" / name).read_bytes()
            print(f"{name}: byte-identical to archived run = {current == archived}")


if __name__ == "__main__":
    main()
