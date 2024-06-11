from typing import Dict, Generic, TypeVar


DictKeys = TypeVar("DictKeys", bound=str)
DictValuesType = TypeVar("DictValuesType")


class GenericDict(Generic[DictKeys,DictValuesType], Dict[DictKeys,DictValuesType]): pass



__all__ = ["GenericDict", "DictValuesType"]