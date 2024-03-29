from django.urls import path, include
from . import views
from accounts import views as AccountView

urlpatterns = [
    path("", AccountView.vendordashboard),
    path("profile/", views.vendorprofile, name="vendorprofile"),
    path("category/", views.menu, name="category"),
    path(
        "category/menus/<int:pk>/",
        views.menusbycategory,
        name="menus_by_category",
    ),
    # Category crud
    path("category/add", views.addcategory, name="add_category"),
    path("category/update/<int:pk>/", views.editcategory, name="edit_category"),
    path("category/delete/<int:pk>/", views.deltecategory, name="delete_category"),
    # menu crud
    path("category/menu/add/", views.addmenu, name="add_menu"),
    path("category/menu/update/<int:pk>/", views.editmenu, name="edit_menu"),
    path("category/menu/delete/<int:pk>/", views.deletemenu, name="delete_menu"),
    # opening hours
    path("openinghours/", views.openinghours, name="opening_hours"),
    path("openinghours/add/", views.addopeninghours, name="add_opening_hours"),
    path(
        "openinghours/delete/<int:id>/",
        views.deleteopeninghours,
        name="delete_opening_hours",
    ),
    # order detail
    path(
        "order-details/<int:order_id>",
        views.vendororderdetails,
        name="vendor_order_details",
    ),
    path("vendor-orders/", views.vendororders, name="vendor_orders"),
    path(
        "vendor-pending-order/", views.vendorpendingorders, name="vendor_pending_orders"
    ),
    path(
        "vendor-process-order/<int:order_id>",
        views.vendorprocessorder,
        name="vendor_process_order",
    ),
    path(
        "vendor-complete-order/<int:order_id>",
        views.vendorcompleteorder,
        name="vendor_complete_order",
    ),
]
