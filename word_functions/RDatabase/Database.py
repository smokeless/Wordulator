class Database():
    """ A dictionary that allows multiple keys for one value """

    def __init__(self):
        self.keys = {}
        self.values = {}


    def __setitem__(self, key, value):
        if key not in self.keys:
            if value not in self.values:  # it's a new value
                self.keys[key] = set()  # a new set
                self.keys[key].add(value)
                self.values[value] = set()  # a new set
                self.values[value].add(key)
            elif value in self.values:
                self.keys[key] = set()  # a new set
                self.keys[key].add(value)
                self.values[value].add(key)  # (1)
            elif key in self.keys:  #
                self.keys[key].add(value)
                if value not in self.values:
                    self.values[value] = set()
                    self.values[value].add(key)
                elif value in self.values:
                    self.values[value].add(key)


    def __delitem__(self, key, value=None):
        if value is None:
            # All the keys relations are to be deleted.
            try:
                value_set = self.keys[key]
                for value in value_set:
                    self.values[value].remove(key)
                    if not self.values[value]:
                        del self.values[value]
                del self.keys[key]  # then we delete the key.
            except KeyError:
                raise KeyError("key not found")
        else:  # then only a single relationships is being removed.
            try:
                if value in self.keys[key]:  # this is a set.
                    self.keys[key].remove(value)
                    self.values[value].remove(key)
                if not self.keys[key]:  # if the set is empty, we remove the key
                    del self.keys[key]
                if not self.values[value]:  # if the set is empty, we remove the value
                    del self.values[value]
            except KeyError:
                raise KeyError("key not found")


    def update(self, key, old_value, new_value):
        if old_value in self.keys[key]:
            affected_keys = self.values[old_value]
            for key in affected_keys:
                self.__setitem__(key, new_value)
                self.keys[key].remove(old_value)
            del self.values[old_value]
        else:
            raise KeyError("key: {} does not have value: {}".format(key, old_value))

    def __getitem__(self, item):
        values = self.keys[item]
        if len(values) > 1:
            return sorted(list(values))
        elif len(values) == 1:
            return list(values)[0]

    def iterload(self, key_list, value_list):
        for key in key_list:
            for value in value_list:
                self.__setitem__(key, value)
