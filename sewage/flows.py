from abc import ABC
from .transforms import transform
from .datastores import DataStore, DataStoreItem

class Job(ABC):
    """
    Take a single item from datastore X and etl it into datastore Y.
    """
    source: DataStoreItem
    target: DataStoreItem # NOTE this doesn't yet exist, of course.

    def etl(self):
        self.target.put(
            item_id=self.target.item_id,
            x=transform(self.source.x, type(self.target.x)),
        )


class Flow(ABC):
    """
    Declare a flow of data from one datastore to another.

    TODO
        - Declare overwrite strategy
        - Address / alert / enforce determinism of output ids
    """
    source: DataStore
    target: DataStore

    def output_id(self, input_id):
        return self.target.item_id_pattern

    def diff(self):
        source_ids = set(self.source.ls())
        target_ids = set(self.target.ls())
        expected_pairs = set((input_id, self.output_id(input_id)) for input_id in source_ids)
        work_to_do = set(p for p in expected_pairs if p[1] not in target_ids)
        for source_id, target_id in work_to_do:
            yield Job(
                # TODO ls() might gen these objects instead
                source=DataStoreItem(item_id=source_id, datastore=self.source),
                target=DataStoreItem(item_id=target_id),
            )

    def sync(self):
        # TODO run serially or in parallel or whatever. MultiProcessingFlow.
        for job in self.diff():
            job.run()
