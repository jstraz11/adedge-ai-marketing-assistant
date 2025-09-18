import numpy as np

def thompson_sampling_allocations(grouped_df):
    """
    grouped_df columns: platform, impressions, conversions, cost
    Model: Beta(successes=conversions+1, failures=(impressions - conversions)+1)
    """
    if grouped_df.empty:
        return []
    samples = []
    for _, row in grouped_df.iterrows():
        impr = max(int(row["impressions"]), 0)
        conv = max(int(row["conversions"]), 0)
        failures = max(impr - conv, 0)
        sample = np.random.beta(conv + 1, failures + 1)
        samples.append((row["platform"], sample))
    vals = np.array([s for _, s in samples], dtype=float)
    exp = np.exp(vals - vals.max())
    shares = exp / exp.sum() if exp.sum() > 0 else np.ones_like(exp)/len(exp)
    out = []
    for (plat, sample), share in zip(samples, shares):
        out.append({"platform": plat, "share": float(share)})
    return out
