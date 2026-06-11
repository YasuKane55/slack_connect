#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""プーブタウン 俯瞰マップ(SVG/PNG)を生成。
クラスター(エリア)＋チップ(各ロケ)方式で、増えたロケーションを全部入れる。
配置ルール反映：こどもプーブリカ=農園敷地内(+ちからこぶ)、商店街アーケード、
長屋、2階建て、巨大倉庫スタジオ、ゆるテーマ＋住宅街に混然、空き物件、エキスペリファーム。
"""
import html

W, H = 1520, 1140
parts = []
def esc(s): return html.escape(s)

def rect(x,y,w,h,fill,stroke="#5b5b5b",rx=12,sw=2,dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,y,s,fs=15,fill="#222",anchor="middle",weight="normal"):
    parts.append(f'<text x="{x}" y="{y}" font-size="{fs}" fill="{fill}" text-anchor="{anchor}" '
                 f'font-weight="{weight}" font-family="IPAGothic, sans-serif">{esc(s)}</text>')

# palette
C_HUB="#ffce6a"; C_FOOD="#ff9b8a"; C_CRAFT="#c9b3f0"; C_LIVE="#a9d3ff"
C_NAT="#a7e0a7"; C_MAT="#dddddd"; C_HOME="#ffe98a"; C_ARC="#e0b483"
C_FARM="#cdeccb"; C_NAGA="#ecd7b0"; C_VAC="#e9e7e0"; C_SEC="#bfe6b0"; C_SENT="#bfe3e8"

def chipw(label):
    return min(300, len(label)*11 + 22)

def zone(x,y,w,h,title,zfill,chips,zstroke="#7a7a7a"):
    """chips: list of (label, color, dash?) """
    rect(x,y,w,h,zfill,stroke=zstroke,rx=16,sw=2)
    text(x+14, y+24, title, fs=15, weight="bold", anchor="start", fill="#333")
    pad=14; cx=x+pad; cy=y+40; rowh=30
    for chip in chips:
        label, col = chip[0], chip[1]
        dash = chip[2] if len(chip)>2 else None
        cw=chipw(label)
        if cx+cw > x+w-pad:
            cx=x+pad; cy+=rowh+6
        rect(cx, cy, cw, rowh, col, rx=8, sw=1.2, stroke="#888", dash=dash)
        text(cx+cw/2, cy+rowh/2+5, label, fs=11, weight="bold")
        cx += cw+8

# bg + title
rect(0,0,W,H,"#f4f7f4",stroke="none",rx=0,sw=0)
text(W/2,38,"プーブタウン ロケーションマップ（v2・全ロケ反映）",fs=24,weight="bold")
text(W/2,62,"ゆるテーマ＋住宅街に混然／中央=みんなのうえん敷地内にこどもプーブリカ／◇花屋台ふ・猫ウルフはランダム出現",fs=13,fill="#555")

# roads (subtle)
parts.append(f'<line x1="40" y1="790" x2="{W-40}" y2="790" stroke="#e9e3d4" stroke-width="18"/>')
parts.append(f'<line x1="760" y1="240" x2="760" y2="790" stroke="#e9e3d4" stroke-width="18"/>')

# === NORTH: 海辺・しぜん ===
zone(40,84,1440,150,"── 北：海辺・しぜん（採集/つり/壁画の名所）──",C_NAT,[
 ("プーブパーク(大きな公園)",C_NAT),("池・川(つり)",C_NAT),
 ("はまべ(貝/砂)",C_NAT),("防潮堤(壁画3枚 A3-5)",C_LIVE),("アート倉庫(屋上=宇宙服猫A11)",C_CRAFT),
])

# === CENTER: みんなのうえん敷地 ===
zone(545,250,420,250,"★中央：みんなのうえん（敷地）",C_FARM,[
 ("★こどもプーブリカ(+ちからこぶ)",C_HUB),("ふんすい広場",C_HOME),
 ("畑(プレイヤー区画)",C_ARC),("のらしごと屋",C_MAT),("もりもり肥料店",C_MAT),
 ("畑アート A15/A17",C_CRAFT),
],zstroke="#5fa15c")

# === WEST: ものづくり・工場 ===
zone(40,250,480,520,"── 西：ものづくり・工場エリア ──",C_CRAFT,[
 ("スーパースタジオ(巨大倉庫2F)",C_CRAFT),("ネンシャ(デザイン)",C_CRAFT),("コトハナ(企画)",C_CRAFT),
 ("ドットアーキ(建築)",C_CRAFT),("塗装アート アンドソー",C_CRAFT),
 ("グッドラック広場(公園)",C_NAT),
 ("工具",C_MAT),("金具",C_MAT),("木材",C_MAT),("工作材料",C_MAT),
 ("家具工場(壁画A13)",C_MAT),("工場1(壁画A31=P)",C_MAT),("工場2(汽車A18)",C_MAT),
 ("工場3(タイポA19)",C_MAT),("倉庫2(顔A9)",C_MAT),
])

# === EAST: たべもの・喫茶 ===
zone(1000,250,480,520,"── 東：たべもの・喫茶エリア ──",C_FOOD,[
 ("中華みんらく",C_FOOD),("オハラカレー&BAR(壁画A22)",C_FOOD),("まるた食堂(朝市)",C_FOOD),
 ("家庭料理こもれび",C_FOOD),("ナチュラルサンド",C_FOOD),("八百屋おやさい本舗",C_NAT),
 ("たこやき たこ天",C_FOOD),("純喫茶こはく",C_FOOD),("ツナグコーヒー",C_LIVE),
 ("長屋:チャイ/サンド/本のすみか(壁画A29)",C_NAGA),
])

# === VACANT: 空き物件・ひみつ（中央下） ===
zone(545,515,420,255,"── 空き物件・ひみつ（まちづくり/探究）──",C_VAC,[
 ("空き家②(A24)",C_VAC,"5 4"),("空き家③(A25)",C_VAC,"5 4"),("空き地①(A23)",C_VAC,"5 4"),
 ("大きな空き地(A26)",C_VAC,"5 4"),("空き工場(A7)",C_VAC,"5 4"),
 ("★シークレットガーデン=エキスペリファーム",C_SEC,"5 4"),
])

# === SOUTH: くらし・商店街・住宅 ===
zone(40,795,1440,235,"── 南：くらし・商店街・住宅エリア（混然）──",C_LIVE,[
 ("プーブ商店街(アーケード):オキ/ヤミー/文房具/雑貨",C_ARC),
 ("2階建て:イエ/サンセール/エトラ/美容室シー",C_NAGA),
 ("リカ公園(小)",C_NAT),("美容室スミス(夜DJ)",C_LIVE),("寿楽温泉(銭湯)",C_SENT),("さんぽや(街歩き案内)",C_LIVE),
 ("ビル1(ロボA28)",C_LIVE),("マンション(A6前/A20壁)",C_LIVE),
 ("住宅1(A16)",C_HOME),("住宅2(お皿A27)",C_HOME),("住宅3(A30)",C_HOME),("住宅4(A21)",C_HOME),
 ("プレイヤーの家",C_HOME),("友達の家(オンライン)",C_HOME),("自分のお店(空き店舗→開業)",C_HOME),
])

# floating: roving + collectibles note
rect(40,1048,1440,72,"#fff",stroke="#ccc",rx=12)
text(60,1072,"◇ 花屋台ふ／猫ウルフ ＝街じゅうにランダム出現",fs=13,weight="bold",anchor="start")
text(60,1096,"● 収集は街じゅうに散在：アート31点 / 猫(ウルフ+主猫) / マンホール10 / 植物(公園・うえん・植木鉢・ベランダぶどう・空き地果物)",fs=12,anchor="start",fill="#555")
# legend
lx=900
text(lx,1072,"凡例:",fs=12,weight="bold",anchor="start")
leg=[("ハブ",C_HUB),("食",C_FOOD),("ものづくり",C_CRAFT),("くらし",C_LIVE),
     ("しぜん",C_NAT),("材料/工場",C_MAT),("住宅",C_HOME),("商店街/長屋",C_ARC),
     ("温泉",C_SENT),("空き(点線)",C_VAC),("探究農園",C_SEC)]
x=lx+48
for name,col in leg:
    rect(x,1062,18,14,col,rx=4,sw=1); text(x+22,1074,name,fs=11,anchor="start"); x+=40+len(name)*12

svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
     + "\n".join(parts) + "\n</svg>\n")
open("map_puubtown.svg","w",encoding="utf-8").write(svg)
print("wrote map_puubtown.svg")
