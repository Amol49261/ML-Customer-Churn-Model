import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# === Load your dataset (adjust path if needed)
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# === Minimal preprocessing
df = df.dropna()
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
X = pd.get_dummies(df.drop('Churn', axis=1), drop_first=True)
y = df['Churn']

# === Train simple model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# === Save artifacts
artifact_dir = "src/serving/model/v1_0/artifacts"
joblib.dump(model, f"{artifact_dir}/model.pkl")
joblib.dump(scaler, f"{artifact_dir}/preprocessing.pkl")

with open(f"{artifact_dir}/feature_columns.txt", "w") as f:
    f.write("\n".join(X.columns))

print("✅ Artifacts saved successfully!")
