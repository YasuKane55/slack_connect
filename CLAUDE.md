# CLAUDE.md — プロジェクトの前提（Claude Code 用メモ）

これは「**ぷーぶ君の まちたんけん（プーブタウン）**」の開発リポジトリです。
新しいセッションは、まず **`README.md`（目次）** と **`GAME_PLAN.md`（企画本体）** を読んでください。

## これは何
- こども向けの生活アドベンチャーゲーム（ブラウザ3D / Three.js）。
- 舞台「プーブタウン」は大阪・北加賀屋の実在店をオマージュした街。
- ねらい：街と関わる楽しさ／自分の“好き”を見つける。
- まず1人用 → 将来オンライン（各自の街＋訪問モデル）。

## いまの状態
- 企画・設定・セリフ・クエスト・地図・各種仕様が **ドキュメントとして完成**。
- **動くルック&フィール・デモ**：`prototype/index.html`（単一HTML・Three.js）。
- 本実装（M1〜）はこれから。順番は `IMPLEMENTATION_READINESS.md` の「推奨ビルド順」。

## ドキュメントの場所（詳細は各 .md）
- 全体：`GAME_PLAN.md` / やさしい版 `READINESS_easy.md` / 実装前 `IMPLEMENTATION_READINESS.md`
- 街・キャラ：`TOWN.md` `CHARACTERS_CONTENT.md` `DIALOGUE.md` `CHAR_DESIGN.md`
- 遊び：`QUESTS_CHAIN.md` `MINIGAMES.md` `SECRET_GARDEN.md` `BALANCE.md`
- 見た目/音/地図/オンライン：`VISUAL.md` `AUDIO.md` `MAP.md` `ONLINE.md`
- マップ画像：`map_puubtown.png`（生成 `tools/generate_map.py`）

## 作るときの方針（大事）
- **やさしい・急かさない・かわいい・さわると気持ちいい**（ねらい§0）。
- 失敗で罰しない。ゲームオーバー無し。報酬は控えめ。
- セリフは**ひらがな多め・短め**。キャラごとに**大阪弁度(0〜3)**と口ぐせを守る（`DIALOGUE.md`）。
- 数値は**1か所(config)に集約**して触りやすく（`BALANCE.md`の仮値）。
- デモの「手応え（ジュース）」を全機能の最低ライン（`VISUAL.md`§4）。

## デモの動かし方（ローカル）
ES Modules/importmap を使うため、**簡易サーバ経由**で開く：
```bash
cd prototype
python3 -m http.server 8000
# ブラウザで http://localhost:8000 を開く
```
（file:// 直開きはモジュール読込でつまずくことあり）

## マップ画像の再生成
```bash
python3 tools/generate_map.py   # SVG生成（PNG化は cairosvg などが必要）
```

## アセットの状態
- ぷーぶ君＝公式PNGは後日。`assets/characters/puub_reference.jpeg` は参考（仮）。
- NPCの絵は**画像生成で作る方針**（`CHAR_DESIGN.md` にプロンプトあり）＝現在は保留。

## 注意・未確定
- 実在のお店/人をモデルにしているので、**公開前に使用許可の確認**（`IMPLEMENTATION_READINESS.md`§7）。
- 技術スタックは、規模的に **Vite等のビルド導入**を検討（プロトはCDN素JS）。
