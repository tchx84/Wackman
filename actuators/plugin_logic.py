# Copyright (c) 2024 Martín Abente Lahaye.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gameeky.common.definitions import State

from gameeky.plugins import Actuator as Plugin


class Actuator(Plugin):
    ended = False

    def tick(self) -> None:
        if self.ended:
            return
        if not self.ready:
            return

        players = []
        coins = []

        # Collect remaining coins and players
        for entity in self.entity.scene.mutables:
            if entity.state == State.DESTROYED:
                continue
            elif entity.playable:
                players.append(entity)
            elif entity.name == "Coin":
                coins.append(entity)

        # Check end conditions
        if len(players) == 0:
            dialogue = "Game Over..."
        elif len(coins) == 0:
            dialogue = "You've Won!"
        else:
            return super().tick()

        # Notify all players
        for player in self.entity.scene.playables:
            player.tell(dialogue)

        self.ended = True
