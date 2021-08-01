class ArrayHelper:
    @staticmethod
    def get(array, key, default=None):
        return array[key] if key in array else default
