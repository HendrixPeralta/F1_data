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
standings = pd.DataFrame(drivers, columns=["driver", "AZE"])
standings.set_index("driver", inplace=True)
# %%
standings.insert(0, 
                 "ITA", 
                 [standings["AZE"]["VER"]-point_system["point"][5],
                  standings["AZE"]["NOR"]-point_system["point"][4]-f_lap,
                  standings["AZE"]["LEC"]-point_system["point"][2],
                  standings["AZE"]["PIA"]-point_system["point"][1]],
                  True)

# %%
standings
# %%
