import json

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

Base = declarative_base()


class AlchemyEncoder(json.JSONEncoder):
    _visited_objs = []
    revisit_self = False

    # TODO : Rewrite this json serializer
    def dict(self):
        fields_to_expand = self._fields_to_expand()
        if isinstance(self.__class__, DeclarativeMeta):
            # don't re-visit self
            if self.revisit_self:
                if self in self._visited_objs:
                    return None
                self._visited_objs.append(self)

            # go through each field in this SQLalchemy class
            fields = {}
            for field in fields_to_expand:
                val = getattr(self, field, None)
                # is this field another SQLalchemy object, or a list of SQLalchemy objects?
                if isinstance(val.__class__, DeclarativeMeta) or (
                        isinstance(val, list) and len(val) > 0 \
                        and isinstance(val[0].__class__, DeclarativeMeta)):
                    # unless we're expanding this field, stop here
                    fields[field] = val.dict()
                else:
                    fields[field] = val
            # a json-encodable dict
            return fields

    def _fields_to_expand(self):
        raise NotImplementedError


class JsonifiableCollection(list):
    def dict(self):
        return list(map(lambda x: x.dict(), self))
