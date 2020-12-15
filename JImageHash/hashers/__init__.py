from ..ji import ji
from ..JImageHash import JImageHash
from .AverageKernelHash import AverageKernelHash
from .DifferenceHash import DifferenceHash

__all__ = ("AverageHash", "AverageKernelHash", "AverageColorHash", "MedianHash", "PerceptiveHash", "RotAverageHash", "RotPHash", "WaveletHash", "DifferenceHash", "HogHash", "HogHashAngularEncoded", "HogHashDual")


class AverageHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.AverageHash(bitsInHash))


class AverageColorHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.AverageColorHash(bitsInHash))


class MedianHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.MedianHash(bitsInHash))


class PerceptiveHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.PerceptiveHash(bitsInHash))


class RotAverageHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.RotAverageHash(bitsInHash))


class RotPHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.RotPHash(bitsInHash))


class WaveletHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64, cycles: int = 18):
		super().__init__(ji.WaveletHash(bitsInHash, cycles))


class WaveletHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64, cycles: int = 18):
		super().__init__(ji.WaveletHash(bitsInHash, cycles))


class HogHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.HogHash(bitsInHash))


class HogHashAngularEncoded(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.HogHashAngularEncoded(bitsInHash))


class HogHashDual(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64):
		super().__init__(ji.HogHashDual(bitsInHash))
