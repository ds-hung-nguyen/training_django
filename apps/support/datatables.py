from apps.support.array_helper import ArrayHelper
from apps.support.helper import constants


class Datatables:
    columns = {}
    query_set = None
    paging_filters = {}
    fields = []

    def __init__(self):
        self.columns = {}
        self.paging_filters = {}
        self.fields = []

    def query_set(self, builder):
        self.query_set = builder
        return self

    def set_paging_filters(self, filters):
        self.paging_filters = filters
        return self

    def selected_fields(self, fields):
        self.fields = fields
        return self

    def set_columns(self, name, content):
        self.columns[name] = content
        return self

    def to_array(self):
        paging_filters = self.__get_paging_filters()
        total_records = self.query_set.count()
        data = list(self.query_set.order_by(paging_filters['order_by'])[paging_filters['start']:paging_filters['start'] + paging_filters['length']].values(*self.fields))
        data = self.__add_columns(data)
        return {
            'recordsTotal': total_records,
            'recordsFiltered': total_records,
            'data': data
        }

    def __add_columns(self, data):
        if self.columns:
            for item in data:
                for (key, value) in self.columns.items():
                    if callable(value):
                        item[key] = value(item)
        return data

    def __get_paging_filters(self):
        filters = {
            'length': int(ArrayHelper.get(self.paging_filters, 'length', constants('PAGE_SIZE_DEFAULT'))),
            'start': int(ArrayHelper.get(self.paging_filters, 'start', 0))
        }
        sort_dir = '-' if ArrayHelper.get(self.paging_filters, 'order[0][dir]', 'desc') == 'desc' else ''
        filters['order_by'] = sort_dir + ArrayHelper.get(self.paging_filters, 'columns[' + ArrayHelper.get(self.paging_filters, 'order[0][column]', 0) + '][data]', 'id')
        return filters
