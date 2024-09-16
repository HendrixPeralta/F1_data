# %%
import pandas as pd 

# %%
f1_points = [[1, 25], [2, 18], [3, 15], [4, 12], [5, 10],
             [6, 8], [7, 6], [8, 4], [8, 2], [10, 1]]

f_lap = 1

point_system = pd.DataFrame(f1_points, columns=["pos", "point"])
point_system.set_index("pos", inplace=True)
point_system.to_csv("./resources/point_system.csv")
# %%
drivers = [["VER",313], ["NOR", 254], ["LEC", 235], ["PIA", 222]]
standings = pd.DataFrame(drivers, columns=["driver", "total"])
standings.set_index("driver", inplace=True)
# %%
standings.insert(1, 
                 "AZE", 
                 [standings["total"]["VER"]-point_system[4],
                  standings["total"]["NOR"]-point_system[3],
                  standings["total"]["VER"]-point_system[4],
                  standings["total"]["VER"]-point_system[4]],
                  True)
# %%
