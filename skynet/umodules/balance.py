# general imports
import peewee as pw

# project imports
import db
import umodule
from utils import exceptions


class UnitProcessor(umodule.UnitProcessor):
    def __init__(self, module_name, unit_name, emoji):
        super().__init__(module_name, unit_name, emoji)

    def subunit_handler(self, words):
        self.subunit = Balance(**self.parse_words(words))
        self.subunit.unit_id = self.unit.id
        self.subunit.save()

    @classmethod
    def parse_words(cls, words: list) -> dict:
        try:
            attributes = {'weight': float(words[0])}
        except (IndexError, ValueError):
            raise exceptions.UnitProcessingError('Specify the weight')

        try:
            attributes['fat'] = float(words[1])
        except (IndexError, ValueError):
            attributes['fat'] = None

        try:
            attributes['water'] = float(words[2])
        except (IndexError, ValueError):
            attributes['water'] = None

        try:
            attributes['muscles'] = float(words[3])
        except (IndexError, ValueError):
            attributes['muscles'] = None

        return attributes


class Balance(db.SubUnit):
    weight = pw.FloatField()
    fat = pw.FloatField(null=True)
    water = pw.FloatField(null=True)
    muscles = pw.FloatField(null=True)
