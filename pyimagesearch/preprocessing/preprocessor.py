import abc


class Preprocessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def preprocess(self, image):
        pass
