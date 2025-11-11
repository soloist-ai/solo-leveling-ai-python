from dataclasses import dataclass
from dataclasses_avroschema import AvroModel


@dataclass
class LocalizationItem(AvroModel):
    en: str
    ru: str

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.localization"
