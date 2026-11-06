# vlm-visual-robustness-skill

VLM（画像も読むモデル）に画像・スクリーンショット・GUI を入力するエージェント向けの
**視覚ディストラクタ堅牢性テスト**を素早く立ち上げるための Claude Code スキル。

タスクと無関係な視覚シンボル（赤いハート・チェックマーク・色つき図形など）が
モデルの判断を歪めていないかを、案件が決まった瞬間に最短手順で検証できるようにする。

## 根拠

- arXiv:2610.36449 *A Heart Means Recursion: Exploring Visual Meaning and Communication in VLMs*（Google DeepMind / Stanford, 2026）
- テスト土台リポ: https://github.com/hiroshi57/vlm-visual-robustness-test

## 中身

```
skills/vlm-visual-robustness/
├── SKILL.md                      # いつ使うか・立ち上げ3ステップ・読み方/直し方
└── templates/
    └── adapter_template.py       # run_task を埋めるだけの雛形
```

## 導入（Claude Code で使う）

スキルフォルダをグローバルのスキル置き場に配置する。

```bash
# 取得
git clone https://github.com/hiroshi57/vlm-visual-robustness-skill

# 配置（Windows の例）
cp -r vlm-visual-robustness-skill/skills/vlm-visual-robustness \
      "$HOME/.claude/skills/"
```

配置後、画像/スクショを VLM に読ませる案件のセッションで、トリガー語
（「画像を読ませるエージェント」「GUIエージェント」「視覚ステアリング」「モデル差し替え」など）
に反応してスキルが発火する。

## 更新の流れ

スキル本体はこのリポで管理し、各自のマシンの `~/.claude/skills/` へ同期する。
手順・判断は SKILL.md、具体コードは土台リポ（vlm-visual-robustness-test）という分担。
