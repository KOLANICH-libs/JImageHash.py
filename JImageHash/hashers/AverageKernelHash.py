import typing

from ..ji import ji
from ..JImageHash import JImageHash
from ..Kernel import Kernel


class AverageKernelHash(JImageHash):
	__slots__ = ()

	def __init__(self, bitsInHash: int = 64, kernels: typing.Optional[typing.Iterable[Kernel]] = None):
		if kernels is None:
			kernels = []

		super().__init__(ji.AverageKernelHash(bitsInHash))
