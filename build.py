"""site/ 원본을 GitHub Pages용 docs/ 로 복사한다. site/index.html 은 head 없이 작성되어 있어 여기서 감싼다."""
import pathlib
import shutil

root = pathlib.Path(__file__).parent
src, out = root / "site", root / "docs"
if out.exists():
    shutil.rmtree(out)
shutil.copytree(src, out)
body = (src / "index.html").read_text(encoding="utf-8")
head = '<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
(out / "index.html").write_text(head + body + "\n</html>\n", encoding="utf-8", newline="\n")
(out / ".nojekyll").write_text("")
print("built", out)
