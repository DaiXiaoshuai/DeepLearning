import abc


class DatasetLoader(metaclass=abc.ABCMeta):
    def __init__(self, preprocessors=None):
        if preprocessors is None:
            self.preprocessors = []

    @abc.abstractmethod
    def load(self, imagePaths):
        pass
