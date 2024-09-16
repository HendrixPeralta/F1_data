# %%
import pandas as pd 

import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches

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

#%%
standings.insert(0, 
                 "NED", 
                 [standings["ITA"]["VER"]-point_system["point"][6],
                  standings["ITA"]["NOR"]-point_system["point"][3]-f_lap,
                  standings["ITA"]["LEC"]-point_system["point"][1],
                  standings["ITA"]["PIA"]-point_system["point"][2]],
                  True)

#%%
standings.insert(0, 
                 "BEL", 
                 [standings["NED"]["VER"]-point_system["point"][2],
                  standings["NED"]["NOR"]-point_system["point"][1]-f_lap,
                  standings["NED"]["LEC"]-point_system["point"][3],
                  standings["NED"]["PIA"]-point_system["point"][4]],
                  True)

# %%
NOR_target = (standings["BEL"]["VER"] -  standings["BEL"]["NOR"])/9
LEC_target = (standings["BEL"]["VER"] -  standings["BEL"]["LEC"])/9
PIA_target = (standings["BEL"]["VER"] -  standings["BEL"]["PIA"])/9

# %%

targets = pd.DataFrame(columns=["driver", "BEL", "NED", "ITA", "AZE"])
# %%

NOR_target_pred = ["NOR_target",
                standings["BEL"]["NOR"], 
                standings["NED"]["VER"] - NOR_target*8, 
                standings["ITA"]["VER"] - NOR_target*7,
                standings["AZE"]["VER"] - NOR_target*6]

targets.loc[0] = NOR_target_pred
# %%
LEC_target_pred = ["LEC_target",
                standings["BEL"]["LEC"], 
                standings["NED"]["VER"] - LEC_target*8, 
                standings["ITA"]["VER"] - LEC_target*7,
                standings["AZE"]["VER"] - LEC_target*6]

targets.loc[1] = LEC_target_pred
# %%
PIA_target_pred = ["PIA_target",
                standings["BEL"]["PIA"], 
                standings["NED"]["VER"] - PIA_target*8, 
                standings["ITA"]["VER"] - PIA_target*7,
                standings["AZE"]["VER"] - PIA_target*6]

targets.loc[2] = PIA_target_pred
# %%
melted_standings = standings.reset_index().melt(id_vars="driver", var_name="GP", value_name="points")
melted_targets = targets.melt(id_vars="driver", var_name="GP", value_name="points")

# %%
palette = ['blue', 'orange', 'red', 'orange']  # Colors for the drivers
linestyles = {'VER': '', 'NOR': '', 'LEC': '', 'PIA': (2, 2)}  # Solid for all except dotted for last driver


palette_target = ['orange', 'red', 'orange']  # Colors for the drivers
linestyles_target = {'NOR_target': '', 'LEC_target': '', 'PIA_target': (2, 2)}  # Solid for all except dotted for last driver

fig, ax = plt.subplots(1, figsize=(12,12))

sns.lineplot(melted_standings, 
             ax=ax,
             x= "GP", 
             y="points",
             hue="driver",
             palette=palette,
             style="driver",
             dashes=linestyles,
             markers=True,
             linewidth=5)

ax.tick_params(axis="x", labelsize=15)
ax.tick_params(axis="y", labelsize=15)

sns.lineplot(melted_targets,
             alpha = 0.4,
             ax=ax, 
             x= "GP", 
             y="points",
             hue="driver",
             palette=palette_target,
             style="driver",
             dashes=linestyles_target,
             markers=True,
             linewidth=3.7)

ax.set_ylabel("Points", fontsize=15, fontdict={"weight":"bold"})
ax.set_xlabel("")

# %%
standings_gap = standings - standings.loc["VER"]
# %%
NOR_target_outscore = (standings_gap["BEL"]["NOR"])/9
LEC_target_outscore = (standings_gap["BEL"]["LEC"])/9
PIA_target_outscore = (standings_gap["BEL"]["PIA"])/9


NOR_target_win = (standings_gap["BEL"]["NOR"]+6)/9
LEC_target_win = (standings_gap["BEL"]["LEC"]+6)/9
PIA_target_win = (standings_gap["BEL"]["PIA"]+6)/9


# %%

targets_outscore = pd.DataFrame(columns=["driver", "BEL", "NED", "ITA", "AZE"])
# %%

NOR_target_outscore_pred = ["NOR target",
                standings_gap["BEL"]["NOR"], 
                standings_gap["BEL"]["NOR"] - NOR_target_outscore, 
                standings_gap["BEL"]["NOR"] - NOR_target_outscore*2,
                standings_gap["BEL"]["NOR"] - NOR_target_outscore*3]

targets_outscore.loc[0] = NOR_target_outscore_pred
# %%
LEC_target_outscore_pred = ["LEC target",
                standings_gap["BEL"]["LEC"], 
                standings_gap["BEL"]["LEC"] - LEC_target_outscore, 
                standings_gap["BEL"]["LEC"] - LEC_target_outscore*2,
                standings_gap["BEL"]["LEC"] - LEC_target_outscore*3]

targets_outscore.loc[1] = LEC_target_outscore_pred
# %%
PIA_target_outscore_pred = ["PIA target",
                standings_gap["BEL"]["PIA"], 
                standings_gap["BEL"]["PIA"] - PIA_target_outscore, 
                standings_gap["BEL"]["PIA"] - PIA_target_outscore*2,
                standings_gap["BEL"]["PIA"] - PIA_target_outscore*3]

targets_outscore.loc[2] = PIA_target_outscore_pred



# %%

targets_win = pd.DataFrame(columns=["driver", "BEL", "NED", "ITA", "AZE"])
# %%

NOR_target_win_pred = ["NOR target",
                standings_gap["BEL"]["NOR"], 
                standings_gap["BEL"]["NOR"] - NOR_target_win, 
                standings_gap["BEL"]["NOR"] - NOR_target_win*2,
                standings_gap["BEL"]["NOR"] - NOR_target_win*3]

targets_win.loc[0] = NOR_target_win_pred
# %%
LEC_target_win_pred = ["LEC target",
                standings_gap["BEL"]["LEC"], 
                standings_gap["BEL"]["LEC"] - LEC_target_win, 
                standings_gap["BEL"]["LEC"] - LEC_target_win*2,
                standings_gap["BEL"]["LEC"] - LEC_target_win*3]

targets_win.loc[1] = LEC_target_win_pred
# %%
PIA_target_win_pred = ["PIA target",
                standings_gap["BEL"]["PIA"], 
                standings_gap["BEL"]["PIA"] - PIA_target_win, 
                standings_gap["BEL"]["PIA"] - PIA_target_win*2,
                standings_gap["BEL"]["PIA"] - PIA_target_win*3]

targets_win.loc[2] = PIA_target_win_pred
# %%

melted_standings_gap = standings_gap.reset_index().melt(id_vars="driver", var_name="GP", value_name="Gap")
melted_targets_outscore = targets_outscore.melt(id_vars="driver", var_name="GP", value_name="Gap")
melted_targets_win = targets_win.melt(id_vars="driver", var_name="GP", value_name="Gap")


# %%
palette = ['blue', 'orange', 'red', 'orange']  # Colors for the drivers
linestyles = {'VER': '', 'NOR': '', 'LEC': '', 'PIA': (2, 2)}  # Solid for all except dotted for last driver


palette_target = ['orange', 'red', 'orange']  # Colors for the drivers
linestyles_target = {'NOR target': '', 'LEC target': '', 'PIA target': (2, 2)}  # Solid for all except dotted for last driver

fig, ax = plt.subplots(1, figsize=(12,12))

sns.lineplot(melted_standings_gap, 
             ax=ax,
             x= "GP", 
             y="Gap",
             hue="driver",
             palette=palette,
             style="driver",
             dashes=linestyles,
             markers=True,
             linewidth=5)

ax.tick_params(axis="x", labelsize=15)
ax.tick_params(axis="y", labelsize=15)

sns.lineplot(melted_targets_outscore,
             alpha = 0.3,
             ax=ax, 
             x= "GP", 
             y="Gap",
             hue="driver",
             palette=palette_target,
             style="driver",
             dashes=linestyles_target,
             markers=True,
             linewidth=3.7)

ax.set_ylabel("Points", fontsize=15, fontdict={"weight":"bold"})
ax.set_xlabel("")

ax.legend(title='Driver and Target', 
                fontsize=13, 
                title_fontsize='15',
                markerscale=2.5, 
                loc='best', 
                bbox_to_anchor=(0.01, 0.5, 0.5, 0.5))
title = "Target to Win the Championship by OUTSCORING VER in the last race"
ax.set_title(title, 
             pad=10,
             fontsize=17,
             fontdict={"weight":"bold"})
# %%
