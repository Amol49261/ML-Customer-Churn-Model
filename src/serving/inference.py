# src/serving/inference.py
from pathlib import Path

def predict(data: dict):
    """
    Return a string/number that your Gradio UI can display.
    """
    try:
        import pandas as pd
        import joblib

        #art = (Path(__file__).resolve().parents[2] / "serving" / "model" / "v1_0" / "artifacts")
        art = Path(__file__).resolve().parent / "model" / "v1_0" / "artifacts"

        model = joblib.load(art / "model.pkl")
        preproc = joblib.load(art / "preprocessing.pkl")
        cols = [c.strip() for c in (art / "feature_columns.txt").read_text().splitlines() if c.strip()]

        df = pd.DataFrame([data])
        for c in cols:
            if c not in df.columns:
                df[c] = None
        X = preproc.transform(df[cols])

        try:
            proba = float(model.predict_proba(X)[0][1])
            return f"Predicted churn={int(proba>=0.5)} (prob={proba:.3f})"
        except Exception:
            return f"Predicted churn={int(model.predict(X)[0])}"
    except Exception as e:
        return f"[inference error] {type(e).__name__}: {e}"
