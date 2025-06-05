from main import X, Y
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = RandomForestRegressor(n_estimators=500, max_features=5, max_samples=0.6, oob_score=True, random_state=42)
rf = model.fit(X_train, Y_train)

joblib.dump(rf, "healthriskscore_model.pkl")

pred_health_risk_score = rf.predict(X_test)

def features():
    print(rf.feature_importances_, rf.feature_names_in_)

def metrics():
    r2 = r2_score(Y_test, pred_health_risk_score)
    print(f'r2 score: {r2}')
    print(f"OOB score: {rf.oob_score_}")