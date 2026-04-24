from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def project_path(*parts):
    return ROOT.joinpath(*parts)
