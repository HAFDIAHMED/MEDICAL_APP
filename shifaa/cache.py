class _BelieveCache:
    """
    A class to have a quick access to data related to exchange values
    """
    _data = dict()

    def get(self, key, defaultvalue):
        if key in self._data:
            return self._data[key]
        return defaultvalue


BELEVE_CACHE = _BelieveCache()
