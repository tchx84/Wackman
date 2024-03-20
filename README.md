# Wackman

A classic arcade game made with and for [Gameeky](https://github.com/tchx84/gameeky).

## Hack it

```
cd ~/Gameeky
git clone https://github.com/tchx84/Wackman.git
```

## Install it as a Flatpak extension

```
git clone https://github.com/tchx84/Wackman.git
cd Wackman
flatpak --user install org.gnome.{Platform,Sdk}//45
flatpak-builder --user --force-clean --install build packaging/dev.tchx84.Gameeky.ThematicPack.Wackman.json
```

## Credits

The [actuators](actuators), [entities](entities) and [scenes](scenes) produced by [Gameeky](https://github.com/tchx84/gameeky) are released under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. These are distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](COPYING) for more details.

The [assets](assets) used in this project belong to opengameart.org and are redistributed under the allowances and limitations of each individual license:

* [20x20 Tileset](https://opengameart.org/content/20x20-tileset) by Lukáš Mrazík. Redistributed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
* [Pacman-clone wakka sound](https://opengameart.org/content/pacman-clone-wakka-sound) by remaxim. Redistributed under [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
* [Pacman-clone Background Music](https://opengameart.org/content/pacman-clone-background-music) by remaxim. Redistributed under [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). 
