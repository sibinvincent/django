from django.urls import path
from .views import IndexView, BookDetail, BookCheckoutView, PaymentComplete, SearchResultsView, LoginGreetView, cart, \
    add_to_cart, remove_from_cart

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('details/<int:pk>/', BookDetail.as_view(), name='details'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout'),
    path('complete/',PaymentComplete, name= 'complete'),
    path('search/',SearchResultsView.as_view(), name='search-results'),
    path('greet/',LoginGreetView.as_view(), name='greet'),
    path('cart/',cart,name='mycart'),
    path('cart/add/<int:book_id>/',add_to_cart,name="add_to_cart"),
    path('cart/remove/<int:book_id>/',remove_from_cart,name="remove_from_cart")
]
