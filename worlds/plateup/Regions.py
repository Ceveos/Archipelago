import typing
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import PlateUpLocation, location_table

plateupareas = ["Overworld"]

def create_regions(world: MultiWorld, player: int):
    regOvr = Region("Overworld", player, world)
    regOvr_names = ["Autumn",  "SantaWorkshopSetting",  "JanuarySetting",  "FebruarySetting",  "MarchSettingTurbo",
                    "JuneSettingCoffeeshop",  "BakerySetting",  "WitchHut2310",  "Alpine",  "City",  "Country",
                    "Halloween",]
    regOvr.locations +=\
        [PlateUpLocation(player, loc_name, location_table[loc_name], regOvr) for loc_name in regOvr_names]
    world.regions.append(regOvr)
