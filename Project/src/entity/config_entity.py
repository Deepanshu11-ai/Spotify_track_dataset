class DataIngestionConfig:
    def __init__(self, source, train_ratio, artifact_dir):
        self.source = source
        self.train_ratio = train_ratio
        self.artifact_dir = artifact_dir