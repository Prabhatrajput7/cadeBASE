from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

"""ONLY WORK WITH VIEWSET OR GENRIC CLASSES"""

class PaginationNum(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'  
    # this with change the page=2 to p=2 
    page_size_query_param = 'size'
    # change the page size accouding to you
    max_page_size = 10
    # max element on a page
    last_page_strings = ('end',)


class PaginationLimit(LimitOffsetPagination):
    """limit is the page size offset is simmply the number of records you wish to skip before selecting record"""
    """ex limit is 5 offset is 12 that means I need 5 items after 12"""
    default_limit = 5 
    max_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'
    # limit_query_param = 'limit' offset_query_param = 'start' checking name of limit and offset


class PaginationCursor(CursorPagination):
    """this wont work with filter"""
    page_size = 5
    ordering = 'created'
    # this is models column created
    cursor_query_param = 'record'
    # this is a parameter instead of cursor it will show record
    #from "http://127.0.0.1:8000/app2/reviewView/?cursor=cD0yMDIyLTA0LTI1KzA3JTNBNDAlM0E1Mi41MTY2MjQlMkIwMCUzQTAw", 
    #to "http://127.0.0.1:8000/app2/reviewView/?record=cD0yMDIyLTA0LTI1KzA3JTNBNDAlM0E1Mi41MTY2MjQlMkIwMCUzQTAw",