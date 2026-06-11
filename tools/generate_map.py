#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""プーブタウン 簡易俯瞰マップ(SVG)を生成する。
配置ルール（farm_site中心/アーケード/長屋/2階建て/巨大倉庫/住宅街に混然）を反映。
ラベルは日本語＝SVGテキストで出力（閲覧側フォントで描画）。
"""
import html

W, H = 1320, 1000
parts = []

def esc(s): return html.escape(s)

def rect(x, y, w, h, fill, stroke="#5b5b5b", rx=10, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

def text(x, y, s, fs=15, fill="#222", anchor="middle", weight="normal"):
    parts.append(f'<text x="{x}" y="{y}" font-size="{fs}" fill="{fill}" '
                 f'text-anchor="{anchor}" font-weight="{weight}" '
                 f'font-family="IPAGothic, sans-serif">{esc(s)}</text>')

def box(x, y, w, h, label, fill, fs=14, sub=None, rx=10):
    rect(x, y, w, h, fill, rx=rx)
    cx = x + w/2
    if sub:
        text(cx, y + h/2 - 4, label, fs=fs, weight="bold")
        text(cx, y + h/2 + 14, sub, fs=fs-3, fill="#444")
    else:
        text(cx, y + h/2 + fs*0.35, label, fs=fs, weight="bold")

def marker(x, y, s, fill):
    parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{fill}" stroke="#fff" stroke-width="2"/>')
    text(x+14, y+5, s, fs=12, anchor="start", fill="#333")

# palette
C_HUB="#ffd27a"; C_FOOD="#ff9b8a"; C_CRAFT="#c9b3f0"; C_LIVE="#a9d3ff"
C_NAT="#a7e0a7"; C_MAT="#d9d9d9"; C_HOME="#ffe98a"; C_ARC="#e0b483"
C_FARM="#cdeccb"; C_NAGA="#ecd7b0"

# background + title
rect(0,0,W,H,"#f4f7f4",stroke="none",rx=0,sw=0)
text(W/2, 38, "プーブタウン 簡易俯瞰マップ（テーマはゆるく・住宅街に混然）", fs=24, weight="bold")
text(W/2, 62, "中央＝みんなのうえん敷地内に こどもプーブリカ／◇花屋台ふ・猫ウルフは街じゅうにランダム出現", fs=14, fill="#555")

# subtle roads
parts.append(f'<line x1="60" y1="500" x2="{W-60}" y2="500" stroke="#e6e0d2" stroke-width="22"/>')
parts.append(f'<line x1="660" y1="120" x2="660" y2="{H-120}" stroke="#e6e0d2" stroke-width="22"/>')

# ---- NORTH: しぜん ----
text(660, 100, "── 北：しぜん（採集・つり） ──", fs=15, fill="#3a7d3a", weight="bold")
box(90, 115, 240, 70, "こうえん", C_NAT, sub="採集・むし・休憩")
box(545, 115, 230, 70, "池・川", C_NAT, sub="つり")
box(990, 115, 240, 70, "はまべ", C_NAT, sub="貝・すな採集")

# ---- CENTER: farm_site ----
rect(455, 350, 410, 290, C_FARM, stroke="#5fa15c", rx=18, sw=3)
text(660, 374, "みんなのうえん（広い敷地）", fs=16, weight="bold", fill="#2f7a2c")
box(470, 388, 185, 40, "のらしごと屋", C_MAT, fs=12)
box(680, 388, 170, 40, "もりもり肥料店", C_MAT, fs=12)
box(540, 442, 240, 70, "★こどもプーブリカ", C_HUB, fs=16, sub="案内・掲示板・称号・朝市")
box(470, 528, 180, 50, "ふんすい広場", "#fff2c2", fs=13, sub="イベント会場")
box(665, 528, 185, 50, "畑（プレイヤー区画）", "#e7c79a", fs=12, sub="種まき→収穫")

# ---- WEST: ものづくり ----
text(235, 215, "── 西：ものづくり寄り ──", fs=15, fill="#6a4fb0", weight="bold")
box(60, 230, 360, 95, "スーパースタジオ（巨大倉庫・2階建て）", C_CRAFT, fs=14,
    sub="1F:モク/ヤタ/マイム/ダイナ ＋DJ  2F:エイ/いろ/パシャ/ぐらこ/ウェブ/ケンチ")
box(60, 340, 110, 48, "ネンシャ", C_CRAFT, fs=12, sub="デザイン")
box(180, 340, 110, 48, "コトハナ", C_CRAFT, fs=12, sub="店メンター")
box(300, 340, 120, 48, "ドットアーキ", C_CRAFT, fs=12, sub="建築")
box(60, 400, 175, 46, "塗装アート アンドソー", C_CRAFT, fs=11, sub="地域・清掃")
box(60, 460, 85, 44, "工具", C_MAT, fs=12)
box(155, 460, 85, 44, "金具", C_MAT, fs=12)
box(250, 460, 85, 44, "木材", C_MAT, fs=12)
box(60, 514, 175, 40, "工作材料 ぺたぺた堂", C_MAT, fs=11)

# ---- EAST: たべもの ----
text(1045, 215, "── 東：たべもの寄り ──", fs=15, fill="#c0503a", weight="bold")
box(885, 230, 150, 46, "中華みんらく", C_FOOD, fs=12)
box(1055, 230, 175, 46, "オハラカレー&BAR", C_FOOD, fs=11)
box(885, 288, 150, 46, "まるた食堂", C_FOOD, fs=12)
box(1055, 288, 175, 46, "家庭料理こもれび", C_FOOD, fs=11)
box(885, 346, 150, 46, "八百屋", C_NAT, fs=12, sub="生鮮")
box(1055, 346, 175, 46, "たこやき たこ天", C_FOOD, fs=11)
box(885, 404, 345, 46, "純喫茶こはく", C_FOOD, fs=12, sub="レトロ喫茶・昔話")
box(885, 462, 345, 46, "トークウィズ チャイ屋は長屋へ（下段）", "#eef0ee", fs=11)

# ---- SOUTH: くらし＆住宅 ----
text(660, 622, "── 南：くらし寄り＆住宅街（混然） ──", fs=15, fill="#2f6db0", weight="bold")
box(60, 638, 560, 92, "プーブ商店街（大型アーケード／屋根付き）", C_ARC, fs=14,
    sub="ブティックオキ｜ちからこぶ｜ヤミーマーケット｜文房具えんぴつ堂｜雑貨マルマル")
box(650, 638, 250, 92, "長屋（3軒つながり）", C_NAGA, fs=13,
    sub="チャイ屋｜ナチュラルサンド｜本のすみか")
box(930, 638, 300, 92, "2階建て（各階2軒）", C_NAGA, fs=13,
    sub="1F イエコーヒー・サンセール / 2F エトラガラス・美容室シー")

box(60, 752, 150, 56, "プレイヤーの家", C_HOME, fs=12, sub="ねる・部屋づくり")
box(225, 752, 160, 56, "自分のお店", C_HOME, fs=12, sub="空き店舗→開業")
box(400, 752, 140, 56, "友達の家", C_HOME, fs=12, sub="(オンライン)")
box(555, 752, 115, 56, "さんぽや", C_LIVE, fs=12, sub="街歩き案内")
box(685, 752, 140, 56, "ツナグコーヒー", C_LIVE, fs=11, sub="休憩")
box(840, 752, 150, 56, "美容室スミス", C_LIVE, fs=11, sub="髪型・夜DJ")

# roving + signatures
rect(1010, 752, 250, 56, "#fff", stroke="#bbb", rx=10)
text(1135, 773, "◇花屋台ふ／猫ウルフ", fs=13, weight="bold")
text(1135, 792, "街じゅうにランダム出現", fs=11, fill="#666")

# art & cat scatter markers（道や余白に配置・箱と重ねない）
for (x,y) in [(435,160),(770,150),(300,595),(1010,595),(645,330),(60,595)]:
    marker(x,y,"アート作品", "#e76f9e")
for (x,y) in [(560,605),(440,300),(905,600),(1085,205)]:
    marker(x,y,"主猫", "#7a5c3a")

# legend
ly = H-58
text(60, ly-8, "凡例：", fs=14, weight="bold", anchor="start")
leg = [("ハブ",C_HUB),("たべもの",C_FOOD),("ものづくり/デザイン",C_CRAFT),
       ("くらし/お店",C_LIVE),("しぜん/農",C_NAT),("材料店",C_MAT),
       ("住宅",C_HOME),("商店街",C_ARC),("長屋/2階建て",C_NAGA)]
x = 110
for name,col in leg:
    rect(x, ly-22, 22, 16, col, rx=4, sw=1)
    text(x+28, ly-9, name, fs=12, anchor="start")
    x += 38 + len(name)*15
marker(x+10, ly-14, "アート作品", "#e76f9e"); x += 150
marker(x+10, ly-14, "主猫", "#7a5c3a")

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">\n' + "\n".join(parts) + "\n</svg>\n")
with open("map_puubtown.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote map_puubtown.svg")
