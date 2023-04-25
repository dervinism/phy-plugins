[Phy](https://github.com/cortex-lab/phy) plugins to help with spikesorting. It contains the following three plugins:
- ```n_spikes_view``` used to adjust the number of displayed waveforms and recording channels in the WaveformView window.
- ```recluster``` plugin providing multiple reclustering actions:
    - Recluster Local PCAs
    - Recluster Global PCAs
    - K means clustering
    - MahalanobisDist
- ```SplitShortISI``` plugin providing a reclustering action to split spikes with the inter-spike interval $\leqslant$ 1.5 ms.

To install plugins, download the contents of this repository (except ```README``` file) and place them inside ```.phy``` folder inside your Windows user directory (```C:\Users\<your-username>\.phy```). Subsequently, open ```phy_config``` file and edit it by replacing ```<your-username>``` entry with the actual name of your user directory.

Plugins were originally created by  for Phy1.
Adapted for Phy2 by Martynas Dervinis.