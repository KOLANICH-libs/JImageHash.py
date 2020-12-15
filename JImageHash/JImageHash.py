from pathlib import Path

import numpy as np
from imagehash import ImageHash
from PIL.Image import Image as PILImage

from .ji import ji

__all__ = ("JImageHash",)


class JImageHash:
	__slots__ = ("hasher",)

	def __init__(self, hasher):
		self.hasher = hasher

	def __call__(self, img) -> ImageHash:
		if isinstance(img, PILImage):
			img = ji.pilImg2JavaImg(img)
		elif isinstance(img, Path):
			f = ji.File(str(img))
			img = ji.ImageIO.read(f)

		res = self.hasher.hash(img)
		hb = np.unpackbits(np.frombuffer(bytes(res.toByteArray()), dtype=np.uint8)).astype(np.bool)
		return ImageHash(hb)
