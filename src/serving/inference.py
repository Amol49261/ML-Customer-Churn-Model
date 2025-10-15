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
        art = Path(__file__).resolve().parent / "model" / "v1.0" / "artifacts"

        model = joblib.load(art / "model.pkl")
        preproc = joblib.load(art / "preprocessing.pkl")
        cols = [c.strip() for c in (art / "feature_columns.txt").read_text().splitlines() if c.strip()]

        df = pd.DataFrame([data])
        
        # Apply the same preprocessing that was done during training
        # Convert binary categorical columns to 0/1
        binary_mappings = {
            'gender': {'Female': 0, 'Male': 1},
            'Partner': {'No': 0, 'Yes': 1},
            'Dependents': {'No': 0, 'Yes': 1},
            'PhoneService': {'No': 0, 'Yes': 1},
            'PaperlessBilling': {'No': 0, 'Yes': 1}
        }
        
        # Apply binary encoding
        for col, mapping in binary_mappings.items():
            if col in df.columns:
                df[col] = df[col].map(mapping).fillna(0)
        
        # Convert numeric columns
        numeric_cols = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        # Handle multi-category columns with one-hot encoding
        multi_cat_columns = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
                           'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
                           'Contract', 'PaymentMethod']
        
        # Create one-hot encoded columns for multi-category variables
        for col in multi_cat_columns:
            if col in df.columns:
                # Create dummy columns for this categorical variable
                for feature_col in cols:
                    if feature_col.startswith(col + '_'):
                        category = feature_col.replace(col + '_', '')
                        df[feature_col] = (df[col] == category).astype(int)
                # Drop the original column
                df = df.drop(columns=[col])
        
        # Ensure all expected columns exist and are numeric
        for c in cols:
            if c not in df.columns:
                df[c] = 0  # Default to 0 for missing features
        
        # Select only the columns the model expects and ensure they're numeric
        X = df[cols].astype(float).fillna(0)

        try:
            proba = float(model.predict_proba(X)[0][1])
            churn_risk = "HIGH RISK" if proba >= 0.5 else "LOW RISK"
            
            if proba >= 0.7:
                message = f"🚨 HIGH CHURN RISK\nCustomer is likely to churn with {proba:.1%} probability"
            elif proba >= 0.5:
                message = f"⚠️ MODERATE CHURN RISK\nCustomer has {proba:.1%} probability of churning"
            elif proba >= 0.3:
                message = f"✅ LOW CHURN RISK\nCustomer has {proba:.1%} probability of churning"
            else:
                message = f"✅ VERY LOW CHURN RISK\nCustomer has {proba:.1%} probability of churning"
                
            return message
        except Exception:
            prediction = int(model.predict(X)[0])
            return "🚨 HIGH CHURN RISK\nCustomer is likely to churn" if prediction == 1 else "✅ LOW CHURN RISK\nCustomer is likely to stay"
    except Exception as e:
        return f"[inference error] {type(e).__name__}: {e}"
