import operator
from functools import reduce

from django.db import models
from rest_framework.compat import distinct
from rest_framework.filters import SearchFilter


class ProCourseCountFilter(SearchFilter):
    search_param = 'proCourseCount'

    def get_search_fields(self, view, request):
        # $ 代表使用 iregex 模式进行字段匹配
        return ['$proCourseCount']
    #
    # def get_search_terms(self, request):
    #     # 获取默认返回的 terms 列表
    #     terms = super().get_search_terms(request)
    #     return [terms]

# 重写此方法参数逻辑改为 or
    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        base = queryset
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.or_, conditions)) # operator.and_ -> operator.or_

        if self.must_call_distinct(queryset, search_fields):
            # Filtering against a many-to-many field requires us to
            # call queryset.distinct() in order to avoid duplicate items
            # in the resulting queryset.
            # We try to avoid this if possible, for performance reasons.
            queryset = distinct(queryset, base)
        return queryset
