"""run_task アダプタのテンプレート。

案件が決まったらこのファイルを対象プロジェクトに複製し、3 箇所（call_agent /
classify / MODEL マッピング）を埋める。vlm-visual-robustness-test リポの
src/adapters.py と同じ契約:

    run_task(model: str, image_path: str, n: int) -> dict[str, float]

返り値はラベル比率（合計 1.0 付近）。例: {"recursive": 0.1, "iterative": 0.9}

使い方:
    VLM_RT_ADAPTER="myproject.vlm_rt:run_task" pytest -q
"""
from __future__ import annotations

from collections import Counter


def proportions(labels: list[str]) -> dict[str, float]:
    if not labels:
        return {}
    c = Counter(labels)
    total = sum(c.values())
    return {k: v / total for k, v in c.items()}


# --- 埋める① 対象エージェントの呼び出し ------------------------------------
def call_agent(model: str, image_path: str) -> str:
    """画像を 1 回入力してエージェントを実行し、生の出力テキストを返す。

    例: 自前 API なら requests.post、SDK なら client.messages.create など。
    秘密はここ（コード側）で読む。LLM コンテキストには結果だけ渡す。
    """
    raise NotImplementedError("対象エージェント呼び出しを実装する")


# --- 埋める② 出力 -> ラベル分類 --------------------------------------------
def classify(output: str) -> str:
    """生出力を 2〜4 個の離散ラベルのどれかに落とす。

    例（コード生成の再帰/反復）:
        return "recursive" if "def " in output and output.count("(") ... else "iterative"
    """
    raise NotImplementedError("出力をラベルに分類する")


# --- 埋める③ モデル識別子（必要なら変換） ----------------------------------
_MODEL_MAP = {
    "default": "claude-opus-4-8",  # tests/test_visual_distractor.py の MODELS に対応
    # "gemini": "gemini-3.1-pro",
    # "gpt": "gpt-5.4",
}


def run_task(model: str, image_path: str, n: int) -> dict[str, float]:
    real_model = _MODEL_MAP.get(model, model)
    labels = [classify(call_agent(real_model, image_path)) for _ in range(n)]
    return proportions(labels)
