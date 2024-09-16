# %%
import pandas as pd 

# %%
f1_points = [[1, 25], [2, 18], [3, 15], [4, 12], [5, 10],
             [6, 8], [7, 6], [8, 4], [8, 2], [10, 1]]

f_lap = 1

point_system = pd.DataFrame(f1_points, columns=["pos", "point"])

point_system.to_csv("./resources/point_system.csv")
# %%
