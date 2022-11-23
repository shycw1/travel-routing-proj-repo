import matplotlib.pyplot as plt
import matplotlib as mpl

# def plot_network(cities, neurons, name='diagram.png', ax=None):
#     mpl.rcParams['agg.path.chunksize'] = 10000
#     if not ax:
#         fig = plt.figure(figsize=(5, 5), frameon = False)
#         axis = fig.add_axes([0,0,1,1])

#         axis.set_aspect('equal', adjustable='datalim')
#         plt.axis('off')

#         axis.scatter(cities['x'], cities['y'], color='red', s=4)
#         axis.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)

#         plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
#         plt.close()

#     else:
#         ax.scatter(cities['x'], cities['y'], color='red', s=4)
#         ax.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)
#         return ax

def plotmap(citydf):
    # plt.plot(citydf['x'], citydf['y'], '.', color='red')

    # plt.show()
    # plt.savefig("city.png")

    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])

    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    axis.scatter(citydf['x'], citydf['y'], color='red', s=4)
    plt.show()
    plt.close()
