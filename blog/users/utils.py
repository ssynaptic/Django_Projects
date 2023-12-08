from pathlib import Path
def handle_uploaded_file(f=None):
    path = Path(__file__).resolve().parent.parent / "media" / "photo-profiles"
    # print(path)
    with open(path / "photo", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)