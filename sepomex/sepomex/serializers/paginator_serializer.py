from django.core.paginator import Paginator


class PaginatorSerializer:

    def __init__(
            self,
            paginator: Paginator,
            page_number: int,
    ):
        self.__paginator = paginator
        self.__page = paginator.get_page(number=page_number)

    def to_dict(self):
        page_number = self.__page.number
        return {
            'page_number': self.__page.number,
            'page_size': self.__paginator.per_page,
            'next_page': page_number+1 if self.__page.has_other_pages() else page_number,
            'total_pages': self.__paginator.num_pages,
        }
