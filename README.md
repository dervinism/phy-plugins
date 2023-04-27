[Phy](https://github.com/cortex-lab/phy) plugins to help with spikesorting. It contains the following three plugins:
- ```n_spikes_view``` used to adjust the number of displayed waveforms and recording channels in the WaveformView window.
- ```recluster``` plugin providing multiple reclustering actions:
    - Recluster PCAs to recluster using klustkwik.
    - K means clustering to recluster using klustkwik with specific number of new clusters.
    - MahalanobisDist to split off outlier spikes deviating by specified standard deviations in the principal component space.
- ```SplitShortISI``` plugin providing a reclustering action to split spikes with the inter-spike interval of $\leqslant$ 1.5 ms.

To install plugins, download the contents of this repository (except ```README``` file) and place them inside ```.phy``` folder inside your Windows user directory (```C:\Users\<your-username>\.phy```). Subsequently, open ```phy_config``` file and edit it by replacing ```<your-username>``` entry with the actual name of your user directory.

Plugins were originally created by Peter Petersen and Thomas Hainmueller for Phy1. \
Adapted for Phy2 by Martynas Dervinis.