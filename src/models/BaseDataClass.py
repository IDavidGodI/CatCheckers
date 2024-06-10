from typing import Type, TypeVar

from dataclasses import fields, dataclass, is_dataclass


T = TypeVar(name="T",bound='ParseableDataClass')

@dataclass
class ParseableDataClass:
  @classmethod
  def from_dict(cls: Type[T], data: dict) -> T:
    kwargs = {}
    for field in fields(cls):
      fieldValue = data.get(field.name)
      if (is_dataclass(field.type) and isinstance(fieldValue, dict)):
        kwargs[field.name] = field.type.from_dict(fieldValue) 
      else:
        kwargs[field.name] = fieldValue
    return cls(**kwargs)