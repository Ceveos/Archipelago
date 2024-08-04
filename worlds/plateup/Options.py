import typing
from dataclasses import dataclass
from Options import Option, DeathLink, Range, Toggle, PerGameCommonOptions

class DoorCost(Range):
    """Amount of Trinkets required to enter Areas. Set to 0 to disable artificial locks."""
    display_name = "Door Cost"
    range_start = 0
    range_end = 3
    default = 3

class AreaCostRandomizer(Toggle):
    """Randomize which Area requires which set of DoorCost Trinkets"""
    display_name = "Area Cost Randomizer"

class ApplianceRandomizer(Toggle):
    """Randomizes which appliance get unlocked"""
    display_name = "Appliance Randomizer"

class SettingCardRandomizer(Toggle):
    """Randomize Setting Cards available"""
    display_name = "Setting Card Randomizer"

@dataclass
class PlateUpOptions(PerGameCommonOptions):
    music_rando: MusicRandomizer
    area_rando: AreaRandomizer
    door_cost: DoorCost
    area_cost: AreaCostRandomizer
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
