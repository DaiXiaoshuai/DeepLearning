import gc
import os

import cv2
import numpy as np
import imutils
from imutils import paths

from pyimagesearch.datasets.datasetloader import DatasetLoader


class SimpleDatasetLoader(DatasetLoader):
    """
    从硬盘上读取图片文件
    """
    def load(self, imagePaths):
        verbose = 10
        data = []
        labels = []
        for (i, imagePath) in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            # /path/to/dataset/{class}/{image}.jpg
            # 文件夹命名时，所有相同label的图片放在以其label命名的文件夹下
            label = imagePath.split(os.path.sep)[-2]
            # 对文件进行预处理
            for preprocessor in self.preprocessors:
                image = preprocessor.preprocess(image)
            data.append(image)
            labels.append(label)
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i + 1, len(imagePaths)))
                gc.collect()
        return np.array(data), np.array(labels)


if __name__ == '__main__':
    path = "F:/PythonProjects/spiderBaidu/cat"
    loader = SimpleDatasetLoader()

    loader.load(list(paths.list_images(path)))
