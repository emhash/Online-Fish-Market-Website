from django.core.paginator import Paginator
from .models import CartItem, Favorite, Order

class ObjectMaster():
    '''Add the Query Object as constructor '''
    def __init__(self, request,the_query=None,):
        self.request = request
        self.the_query=the_query

    def Paginate(self, query=None , no_of_object = 5):
        if query is None:
            query=self.the_query

        '''In this method pass how many object per page you want to show if you wish. '''
        if self.the_query:
            # ==--------PAGINATION ------==
            pg = Paginator( query, no_of_object)
            page_number = self.request.GET.get('page')
            q_per_page = pg.get_page(page_number)

        else:
            q_per_page = None
            print("Add an object to perform pagination adding.")
        
        return q_per_page

    def Searching(self, FilteredQuery):
        '''If a Query added as constructor, pass the Filtered Query here'''
        if self.the_query:
            # ----- ADD SEARCH OPTION -----
            search_option = FilteredQuery(self.request.GET, queryset=self.the_query)
            filtered_query = search_option.qs
        else:
            search_option = None
            filtered_query = None
            print('Add a query object as constructor.')

        return search_option , filtered_query

'''
<form method="GET">
    {% for field in searching.form %}
    {{ field.label }}
    {{ field }}
    {% endfor %}
    <button> Submit </button>
</form>

'''
