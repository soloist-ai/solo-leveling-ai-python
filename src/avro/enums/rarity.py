from enum import Enum


class Rarity(str, Enum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.player"
