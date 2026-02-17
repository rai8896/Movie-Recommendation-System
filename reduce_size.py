import numpy as np
import joblib

similarity = joblib.load("similarity.pkl")

similarity = np.round(similarity, 2)   # try 2 or even 1

joblib.dump(similarity, "similarity_small.pkl", compress=5)
