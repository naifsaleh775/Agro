from django.urls import path
from . import views

urlpatterns=[
    path('user_page' , views.index , name='index_page'),
    path('user_outputShipping/<int:sh_id>' , views.user_outputShipping , name='user_outputShipping'),
    path('socialMessages' , views.socialMessages , name='socialMessages'),
    path('profile_list' , views.profileList , name='profileList'),
    path('profile/<int:pk>' , views.profile , name='profile'),
    path('update_user_profile' , views.update_user_profile , name='update_user_profile'),
    
    # Authentication URLS........................................................
    path('' , views.login_user , name='login_user'),
    path('logout_user' , views.logout_user , name='logout_user'),
    path('register_user' , views.register_user , name='register_user'),
    # Managment URLS...............................................................
    # Supliers URLS...
    path('index_dashboard/' ,views.dashboard, name='index_dashboard'),
    path('suppliers/' ,views.suppliersPage, name='supplier'),
    path('deleteSupplier/<int:sp_id>' ,views.deleteSupplier, name='deleteSupplier'),
    path('supplierInfo/<int:sp_id>' ,views.supplierInfo, name='supplierInfo'),
    path('editSupplier/<int:sp_id>/' ,views.editSupplier, name='editSupplier'),
    path('updateSupplier/<int:sp_id>' ,views.updateSupplier, name='updateSupplier'),
   
    # Shippings URLS...................................................................
    path('shipping/' ,views.shippingPage, name='shipping'),
    path('deleteShipping/<int:sh_id>' ,views.deleteShipping, name='deleteShipping'),
    path('shippingInfo/<int:sh_id>' ,views.shippingInfo, name='shippingInfo'),
    path('editShipping/<int:sh_id>' ,views.editShipping, name='editShipping'),
    path('updateShipping/<int:sh_id>' ,views.updateShipping, name='updateShipping'),
    path('AddShippingDirectionModal' ,views.AddShippingDirectionModal, name='AddShippingDirectionModal'),
    path('add_shipping_direction_modal' ,views.add_shipping_direction_modal, name='add_shipping_direction_modal'),

    #Shipping Direction URLS............................................................
     path('shippingDirection/' ,views.shippingDirectionPage, name='shippingDirectionPage'),
     path('deleteShippingDirection/<int:sh_id>' ,views.deleteShippingDirection, name='deleteShippingDirection'),
     path('editShippingDirection/<int:sh_id>' ,views.editShippingDirection, name='editShippingDirection'),
     path('updateShippingDirection/<int:sh_id>' ,views.updateShippingDirection, name='updateShippingDirection'),
     
    # Sticking URLS.....................................................................
    path('sticking/' ,views.stickingPage, name='stickingPage'),
    path('deleteSticking/<int:st_id>' ,views.deleteSticking, name='deleteSticking'),
    path('stickingInfo/<int:st_id>' ,views.stickingInfo, name='stickingInfo'),
    path('editSticking/<int:st_id>' ,views.editSticking, name='editSticking'),
    path('updateSticking/<int:st_id>' ,views.updateSticking, name='updateSticking'),
    path('addStickerModal' ,views.addStickerModal, name='addStickerModal'),
    path('add_sticker_modal' ,views.add_sticker_modal, name='add_sticker_modal'),

    # Cartoons URLS.....................................................................
    path('cartoons/' ,views.cartoonPage, name='cartoonPage'),
    path('deleteCartoon/<int:cr_id>' ,views.deleteCartoon, name='deleteCartoon'),
    path('cartoonInfo/<int:cr_id>' ,views.cartoonInfo, name='cartoonInfo'),
    path('editCartoon/<int:cr_id>' ,views.editCartoon, name='editCartoon'),
    path('updateCartoon/<int:cr_id>' ,views.updateCartoon, name='updateCartoon'),
    path('AddCartoonModal' ,views.AddCartoonModal, name='AddCartoonModal'),
    path('add_cartoon_modal' ,views.add_cartoon_modal, name='add_cartoon_modal'),



    # Oil Suppliers URLS..................................................................
    path('oilSupplierPage/' ,views.oilSupplierPage, name='oilSupplierPage'),
    path('deleteOilSupplier/<int:oi_id>' ,views.deleteOilSupplier, name='deleteOilSupplier'),
    path('oilInfo/<int:oi_id>' ,views.oilInfo, name='oilInfo'),
    path('editOilSupplier/<int:oi_id>' ,views.editOilSupplier, name='editOilSupplier'),
    path('updateOilSupplier/<int:oi_id>' ,views.updateOilSupplier, name='updateOilSupplier'),
    path('addOilSuplierModal' ,views.addOilSuplierModal, name='addOilSuplierModal'),
    path('add_oil_suplier_modal' ,views.add_oil_suplier_modal, name='add_oil_suplier_modal'),


    # Certifications URLS..................................................................
    path('certificationPage/' ,views.certificationPage, name='certificationPage'),
    path('certificationDelete/<int:ce_id>' ,views.certificationDelete, name='certificationDelete'),
    path('certificationEdit/<int:ce_id>' ,views.certificationEdit, name='certificationEdit'),
    path('certificattionInfo/<int:ce_id>' ,views.certificattionInfo, name='certificattionInfo'),
    path('certificattionUpdate/<int:ce_id>' ,views.certificattionUpdate, name='certificattionUpdate'),



    # Packging Processing and Loading URLS.............................................
    path('packgingProcessing/' ,views.packgingProcessing, name='packgingProcessing'),
    path('outPutShipping/<int:sh_id> ' ,views.outPutPage, name='outPutPage'),
    path('outPutShipping_pdf/<int:sh_id> ' ,views.outPutPage_pdf, name='outPutPage_pdf'),







    path('dataTable/' ,views.dataTable, name='dataTable'),
    path('myProfile/' ,views.myProfile, name="myProfile"),
    path('contactAdmin/' ,views.contactAdmin, name="contactAdmin"),
    path('userMessage/' ,views.userMessage, name="userMessage"),
]