from typing import Type, TypeVar

from dataclasses import fields, dataclass, is_dataclass

from models.genericDicts import GenericDict



T = TypeVar(name="T",bound='ParseableDataClass')

def _get_genericdict_values_type(testType):

  if issubclass(testType,(GenericDict)):
    if (hasattr(testType, "__args__")):
      print(testType, testType.__args__[-1])
      return testType.__args__[-1]
    # if (DictValuesType in testType.__parameters__): return
    for cls in testType.__orig_bases__:
      subcls = _get_genericdict_values_type(cls)
      if (subcls):
        return subcls

@dataclass
class ParseableDataClass:

  @classmethod
  def from_dict(cls: Type[T], data: dict) -> T:
    kwargs = {}
    
    for field in fields(cls):
      fieldValue = data.get(field.name)
      if (isinstance(fieldValue, (dict))):
        if (is_dataclass(field.type)):
          kwargs[field.name] = field.type.from_dict(fieldValue) 
        else:
         
          subtype = _get_genericdict_values_type(field.type)
            
          

          if is_dataclass(subtype):
            subdata = {}
            for k,v in fieldValue.items():
              
              subdata[k] = subtype.from_dict(v)
            
            kwargs[field.name] = subdata
          else:
            kwargs[field.name] = fieldValue
      else:
        kwargs[field.name] = fieldValue
        
    return cls(**kwargs)
  

__all__ = ["ParseableDataClass"]