# データ指向アプリケーションデザイン クイズ

『データ指向アプリケーションデザイン 第2版』の章ごとのスライドとクイズです。章の内容をスライドでおさらいしてから、選択式の問題を解き、最後に自分たちのシステムに当てはめて話します。

問題の誤りの指摘や改善、新しい章の追加は、プルリクエストで受け付けています。

## 見る

このリポジトリはprivateなので、GitHub Pagesでは公開していません。手元でビルドして開きます。必要なのはPythonだけです。

```sh
python3 tools/build.py
open dist/ch01/index.html
```

GitHub Actionsの実行結果からも、ビルド済みの `dist` をダウンロードできます。

## ディレクトリ構成

| パス | 内容 |
|---|---|
| `src/index.html` | 章の一覧ページ |
| `src/engine.html` | 全章で共通の画面と動作 |
| `src/chapters/chNN.js` | 章ごとのスライドと問題 |
| `summaries/chNN.md` | 章のサマリー（Markdown） |
| `tools/build.py` | `src/` から `dist/` を作る |
| `tools/check.js` | `dist/` の全スライドを描画し、問題の書き方の誤りを調べる |

## 問題を直す・追加する

問題は `src/chapters/chNN.js` の `SLIDES` にあります。1問は次の形で書きます。

```js
{
  type: "q", sec: "1.1.3 記録のシステムと導出データ", title: "検索インデックスが消えた", ref: "derived",
  prompt: "問題文",
  choices: [
    { text: "選択肢の文", ok: true, note: "この選択肢の解説" },
    { text: "選択肢の文", ok: false, note: "この選択肢の解説" },
  ],
  takeaway: "回答後に表示するまとめ。<b>強調したい一文</b>",
},
```

| キー | 意味 |
|---|---|
| `sec` | 本の節の番号と見出し |
| `ok` | 正解なら `true`。1問に1つだけ |
| `ref` | 関連するスライド（`type: "intro"`）の `id` |
| `aside` | 右側に補足のパネルを出すときの、HTMLを返す関数（省略できる） |

スライドの種類は次のとおりです。

| `type` | 内容 |
|---|---|
| `cover` | 表紙 |
| `intro` | 章の内容をおさらいするスライド。本文は `INTRO_BODY[id]` に書く |
| `q` | 選択式の問題 |
| `talk` | 正解のない問いを並べて、みんなで話すスライド |
| `end` | 正解数とまとめ |

直したら、手元で次を実行して確認します。Node.jsも必要です。

```sh
python3 tools/build.py
node tools/check.js
```

## 新しい章を足す

1. `src/chapters/ch01.js` をコピーして `chNN.js` を作り、`CH`・`SLIDES`・`INTRO_BODY` を書き換える
2. `src/index.html` の一覧に章を足す
3. 章のサマリーがあれば `summaries/chNN.md` に置く
