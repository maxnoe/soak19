from soak19 import plot_xyz_gamut, cmf
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
w, h = fig.get_size_inches()
fig.set_size_inches(h, h)

ax = fig.add_subplot(1, 1, 1)
plot_xyz_gamut(ax=ax, wavelengths=False)


ax.plot(
    [0.64, 0.21, 0.15, 0.64], [0.33, 0.71, 0.06, 0.33],
    marker='.', ls='-', color='lightgray',
    label='AdobeRGB',
)

ax.plot(
    [0.64, 0.3, 0.15, 0.64], [0.33, 0.6, 0.06, 0.33],
    marker='.', ls='-', color='k',
    label='sRGB',
)

ax.legend()

fig.savefig('build/plots/gamut_srgb.pdf')
