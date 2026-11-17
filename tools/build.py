"""src/ から dist/ を作る。

使い方: python3 tools/build.py
章ごとに src/engine.html へ src/chapters/chNN.js を埋め込み、
1ファイルで動く dist/chNN/index.html を書き出す。
"""
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"


def main():
    shutil.rmtree(DIST, ignore_errors=True)
    DIST.mkdir()
    shutil.copy(SRC / "index.html", DIST / "index.html")
    engine = (SRC / "engine.html").read_text()
    for chapter in sorted((SRC / "chapters").glob("ch*.js")):
        name = chapter.stem
        html = (
            engine.replace("/*TITLE*/", f"データ指向アプリケーションデザイン {int(name[2:])}章クイズ")
            .replace("/*CHAPTER*/", chapter.read_text())
        )
        (DIST / name).mkdir()
        (DIST / name / "index.html").write_text(html)
        print(f"dist/{name}/index.html")


if __name__ == "__main__":
    main()
