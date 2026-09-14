import csv
import pathlib
from abc import ABC

class DataStore(ABC):
    """
    TODO Force overrides of ls, get, put?
    """

    def __init__(self, model):
        self.model = model
        self.data = {}

    def ls(self):
        return set(self.data.keys())

    def get(self, item_id):
        return self.data.get(item_id)

    def put(self, item_id, x):
        self.data[item_id] = x

class DataStoreItem(ABC):
    def __init__(self, datastore, item_id):
        self.datastore = datastore
        self.item_id = item_id

    def get(self):
        return self.datastore.get(self.item_id)

class CsvFileStore(DataStore):
    def __init__(self, path):
        self.path = pathlib.Path(path)

    def item_ref(self, item_id):
        """
        Translates an item_id to its actual convenient reference.

        NOTE Necessary in base DataStore class?
        No, right, bc get and put are easy to define?
        """
        return self.path / f'{item_id}.csv'

    def ls(self):
        for f in self.path.glob('*.csv'):
            if f.is_file():
                yield f.root

    def get(self, item_id):
        with open(self.item_ref(item_id)) as f:
            for r in csv.DictReader(f):
                yield r

    def put(self, item_id, x):
        with open(self.item_ref(item_id), 'w') as f:
            field_names = x[0].keys()
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for record in x:
                writer.writerow(record)
