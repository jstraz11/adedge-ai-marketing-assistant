import os
import pandas as pd
import numpy as np
from .features import build_features

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def train_lightgbm_stub(settings):
    """
    Train a tiny LightGBM model on synthetic data with a median-split label.
    Saves to settings.model_dir/audience_model.txt and returns the path.
    """
    try:
        import lightgbm as lgb
    except Exception as e:
        raise RuntimeError(f"LightGBM not installed correctly: {e}")

    _ensure_dir(settings.model_dir)

    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "feature_1": rng.normal(0,1,1000),
        "feature_2": rng.integers(0,10,1000),
        "feature_3": rng.uniform(0,1,1000),
    })
    X = build_features(df)
    y = (X["feature_1"] > X["feature_1"].median()).astype(int)

    dtrain = lgb.Dataset(X, label=y)
    params = {"objective":"binary", "metric":"auc", "verbosity":-1}
    model = lgb.train(params, dtrain, num_boost_round=50)
    model_path = os.path.join(settings.model_dir, "audience_model.txt")
    model.save_model(model_path)
    return model_path
