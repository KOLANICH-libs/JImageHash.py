from enum import Enum
from pathlib import Path
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/JImageHash.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

import JAbs
import numpy as np
from imagehash import ImageHash
from PIL.Image import Image as PILImage

from .hashers import *
from .ji import ji
from .Kernel import *
