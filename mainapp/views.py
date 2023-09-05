from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Profile , User , Twieet , Supplier , Shipping , Sticker , Cartoon , OilSupplier , Certificate , ShippingDirection
from django.contrib import messages
from .form import TwieetForm , SignUpForm 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Generate PDF File

# Create your views here.
def socialMessages(request):
    twieetCount = Twieet.objects.count()
    if request.user.is_authenticated:
        form = TwieetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                twieet = form.save(commit=False)
                twieet.user = request.user
                twieet.save()
                messages.info(request , 'Message Sent Successfully')
                return redirect('socialMessages')
        twieets = Twieet.objects.all().order_by('-created_at')
        return render(request , 'user/socialMessages.html' , {'twieets':twieets , 'form':form })
    else:
        twieets = Twieet.objects.all().order_by('-created_at')
        return render(request , 'user/socialMessages.html' , {'twieets':twieets, 'twieetCount':twieetCount})
    

def index(request):
    shippings = ShippingDirection.objects.all()
    return render(request , 'user/index.html' , {'shippings':shippings})

def user_outputShipping(requset , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    shippings = Shipping.objects.filter(direction__id=sh_id)
    # shippings = ShippingDirection.objects.get(id=sh_id)
    import datetime
    now = datetime.datetime.now()
    context={
        'shippings':shippings,
        'direction':direction,
        'now':now
    }
    return render(requset ,  'user/user_outputShipping.html' , context)



def profileList(request):
    if request.user.is_authenticated:
        profiles_user = Profile.objects.exclude(user=request.user)
        users = User.objects.all()
        profiles = Profile.objects.all()
        return render(request , 'profile_list.html' , {'users':users , 'profiles':profiles , 'profiles_user':profiles_user})
    else:
        messages.info(request , 'You Must Login First')
        return redirect('login_user')
    

def profile(request , pk): 
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        twieets = Twieet.objects.filter(user_id = pk).order_by('-created_at')
        twieetCount = Twieet.objects.count()
        # Logic........
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST["follow"]
            if action == "unfollow":
                current_user_profile.followes.remove(profile)
            elif action == "follow":
                current_user_profile.followes.add(profile)
                current_user_profile.save()
        return render(request , 'user/profile.html' , {'profile':profile , 'twieets':twieets , 'twieetCount':twieetCount })
    else:
        messages.info(request , 'You Must Login First')
        return redirect('login_user')
    

def update_user_profile(request):
    return render(request , 'user/update_user_profile.html')
    

def login_user(request):
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request , username=username , password=password)
       
       if  user.is_staff == True:
            login(request , user)
            messages.info(request , 'Welcom '+request.user.username+" your authrized as Admin")
            return redirect('index_dashboard')
       elif user is not None:
            
            login(request , user)
            return redirect("index_page")
       else:
           messages.info(request , 'Check out your username or password')
           return redirect('login_user')
   return render(request , 'admin/login_user.html')

def logout_user(request):
    logout(request)
    messages.info(request , '')
    return redirect('login_user')

def register_user(request):
    if request.method == "POST":
       form = SignUpForm(request.POST)
       if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'You are really regitred ' + user)
            return redirect('login_user')
    else:
        form = SignUpForm()
    return render(request , 'admin/register_user.html' , {'form':form})
    

def dashboard(request):
    supplier = Supplier.objects.count()
    shipping = Shipping.objects.count()
    sticker = Sticker.objects.count()
    cartoon = Cartoon.objects.count()
    certification = Certificate.objects.count()
    oil_supplier = OilSupplier.objects.count()
    context = {
        'supplier':supplier,
        'shipping':shipping,
        'sticker':sticker,
        'cartoon':cartoon,
        'certification':certification,
        'oil_supplier':oil_supplier
    }
    if request.user.is_authenticated:
        if request.user.username == "admin":
            return render(request , 'admin/index_dashboard.html' , context)
        else:
            messages.error(request , "Soory, you are not admin")
            return redirect('/')
    else:
        messages.info(request , 'You Must Login First')
        return redirect('login_user')
    

# Suppliers Views.......................................................................
def suppliersPage(request):
    supplier = Supplier.objects.order_by('-created_at')
    sticker_info = Sticker.objects.all()
    shippings = Shipping.objects.all()
    supplier_Oil = OilSupplier.objects.all()
    cartoons = Cartoon.objects.all()
    if request.method == "POST":
       supplier_name = request.POST['supplier']
       jon_size = request.POST['jon_size']
       jon_count = request.POST['jon_count']
       jon_price = request.POST['jon_price']
       jon_ton_liter = request.POST['jon_ton_liter']
       sticker = request.POST['sticker']
       jerecan_oil = request.POST['oil_supplier']
       cartoon = request.POST['cartoon']

       info = Supplier(supplier_name=supplier_name , jerecan_oil_id=jerecan_oil , jon_size=jon_size, jon_count=jon_count , joi_price=jon_price , value_ofTonToLiter=jon_ton_liter, jerecan_sticker_id=sticker , cartoon_id=cartoon )
       info.save()
       messages.success(request , 'Supplier Saved Successfully')
       return redirect('supplier')
    return render(request , 'management/suppliers.html' , {'supplier':supplier , 'supplier_Oil':supplier_Oil , 'shippings':shippings, 'sticker_info':sticker_info , 'cartoons':cartoons} )

def deleteSupplier(requst , sp_id):
    supplier = Supplier.objects.get(id=sp_id)
    supplier.delete()
    messages.success(requst , 'Supplier Deleted Successfully')
    return redirect('supplier')

def supplierInfo(request , sp_id):
    supplier_info = Supplier.objects.get(id=sp_id)
    supplier = supplier_info.jon_size*supplier_info.jon_count
    fixed = 1000
    tonByLiter = supplier_info.value_ofTonToLiter + 6 
    
    return render(request , 'management/supplier_info.html' , {'tonByLiter':tonByLiter,'supplier_info':supplier_info , 'supplier':supplier , 'fixed':fixed})

def editSupplier(request , sp_id):
    modify = Supplier.objects.get(id=sp_id)
    sticker_info = Sticker.objects.all()
    oil_suppliers = OilSupplier.objects.all()
    return render(request , 'management/editSupplier.html' , {'modify':modify , 'oil_suppliers':oil_suppliers , 'sticker_info':sticker_info} )

def updateSupplier(request , sp_id):

    supplier = Supplier.objects.get(id = sp_id)
    supplier.supplier_name = request.POST['supplier']
    supplier.jon_size = request.POST['jon_size']
    supplier.jon_count = request.POST['jon_count']
    supplier.joi_price = request.POST['jon_price']
    supplier.jerecan_sticker_id = request.POST['sticker']
    supplier.value_ofTonToLiter = request.POST['jon_ton_liter']
    supplier.jerecan_sticker_id = request.POST['sticker']
    supplier.save()
    messages.info(request , "Supplier Updated Successfully")
    return redirect("/suppliers")
    

# Shipping Views...................................................................
def shippingPage(request):
    shippings = Shipping.objects.order_by('-created_at')
    direction = ShippingDirection.objects.all()
    jerecans = Supplier.objects.all()
    cretifications = Certificate.objects.all()
    if request.method == "POST":
       shipping_name = request.POST['shipping_name']
       direction = request.POST['direction']
       shipping_price = request.POST['shipping_price']
       shipping_date = request.POST['shipping_date']
       shipping_time = request.POST['shippin_time']
       certification_type = request.POST['certification_type']
       jerecan_type = request.POST['Jerecan']
       grossing = request.POST['grossing']
       margin = request.POST['margin']
       
       info = Shipping(company_name=shipping_name , trip_Price=shipping_price , grossing=grossing , margin=margin , trip_date= shipping_date, trip_Time=shipping_time , direction_id=direction , jerecan_id = jerecan_type , certification_id=certification_type)
       info.save()
       messages.success(request , 'Shipping Saved Successfully')
       return redirect('/shipping')
    return render(request , 'management/shipping.html' , {'shippings':shippings , 'cretifications':cretifications , 'jerecans':jerecans , 'direction':direction})


def deleteShipping(request , sh_id):
    shipping = Shipping.objects.get(id=sh_id)
    shipping.delete()
    messages.success(request , 'Shipping Deleted Successfully')
    return redirect('shipping')

def shippingInfo(request , sh_id):
    shipping_info = Shipping.objects.get(id=sh_id)
    jerecan = Shipping.objects.get(id = sh_id)
    return render(request , 'management/shipping_info.html' , {'shipping_info':shipping_info , 'jerecan':jerecan})

def editShipping(request , sh_id):
    jerecan = Supplier.objects.all()
    cretifications = Certificate.objects.all()
    direction = ShippingDirection.objects.all()
    shipping = Shipping.objects.get(id=sh_id)
    return render(request , 'management/editShipping.html' , {'shipping':shipping , 'direction':direction ,'cretifications':cretifications , 'jerecan':jerecan})


def updateShipping(request , sh_id):
    shipping = Shipping.objects.get(id = sh_id)
    shipping.company_name = request.POST['shipping_name']
    shipping.trip_Price = request.POST['shipping_price']
    shipping.direction_id = request.POST['direction']
    shipping.jerecan_id = request.POST['Jerecan']
    shipping.certification_id = request.POST['certification_type']
    shipping.trip_date = request.POST['shipping_date']
    shipping.trip_Time = request.POST['shipping_time']
    shipping.grossing = request.POST['grossing']
    shipping.margin = request.POST['margin']
    shipping.save()
    messages.info(request , "Shipping Updated Successfully")
    return redirect("/shipping")


#Shipping Direction Views..........................................................
def shippingDirectionPage(request):
    direction = ShippingDirection.objects.all()
    
    if request.method == "POST":
        direction = request.POST['direction']
        shipping_direction = ShippingDirection(direction=direction )
        shipping_direction.save()
        messages.info(request , "Shipping Direction Added Successfully")
        return redirect('shippingDirectionPage')
    return render(request , 'management/shippingDirection.html' , {'direction':direction})

def AddShippingDirectionModal(request):
    return render(request , 'management/AddShippingDirectionModal.html')

def add_shipping_direction_modal(request):
    direction = request.POST['direction']
    shipping_direction = ShippingDirection(direction=direction )
    shipping_direction.save()
    messages.info(request , "Shipping Direction Added Successfully")
    return redirect('shipping')

def deleteShippingDirection(request , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    direction.delete()
    messages.info(request , "Shipping Direction Deleted Successfully")
    return redirect('shippingDirectionPage')

def editShippingDirection(request , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    shipping = Shipping.objects.all()
    return render(request , 'management/editShippingDirection.html' , {'direction':direction , 'shipping':shipping})


def updateShippingDirection(request , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    direction.direction = request.POST['direction']
    
    direction.save()
    messages.info(request , "Shipping Direction Updated Successfully")
    return redirect('shippingDirectionPage')





# Sticking Views....................................................................
def stickingPage(request):
    stickers = Sticker.objects.order_by('-created_at')
    jerecan = Supplier.objects.all()
    if request.method == "POST":
        sticker_company = request.POST['sticker_company']
        sticker_size = request.POST['sticker_size']
        sticker_price = request.POST['sticker_price']
        sticker = Sticker(sticker_company=sticker_company,sticker_price=sticker_price,sticker_size=sticker_size)
        sticker.save()
        messages.success(request , 'Sticker Added Successfully')
        redirect('stickingPage')
    return render(request , 'management/sticker.html' , {'stickers':stickers ,'jerecan':jerecan})

def addStickerModal(request):
    return render(request , 'management/AddStickerModal.html')

def add_sticker_modal(request):
    sticker_company = request.POST['sticker_company']
    sticker_size = request.POST['sticker_size']
    sticker_price = request.POST['sticker_price']
    sticker = Sticker(sticker_company=sticker_company,sticker_price=sticker_price,sticker_size=sticker_size)
    sticker.save()
    messages.success(request , 'Sticker Added Successfully')
    return redirect('supplier')


def deleteSticking(request , st_id):
    sticker = Sticker.objects.get(id=st_id)
    sticker.delete()
    messages.success(request , 'Sticker Deleted Successfully')
    return redirect('stickingPage')

def stickingInfo(request , st_id):
    sticker = Sticker.objects.get(id=st_id)
    return render(request , 'management/sticker_info.html' , {'sticker':sticker})

def editSticking(request , st_id):
    sticker = Sticker.objects.get(id=st_id)
    jerecan_size = Supplier.objects.all()
    return render(request , 'management/editSticking.html' , {'sticker':sticker , 'jerecan_size':jerecan_size})


def updateSticking(request , st_id):
    sticker = Sticker.objects.get(id=st_id)
    sticker.sticker_company = request.POST['sticker_company']
    sticker.sticker_price = request.POST['sticker_price']
    sticker.sticker_size = request.POST['sticker_size']
    sticker.save()
    messages.success(request , 'Sticker Updated Successfully')
    return redirect('stickingPage')


# Cartoon Views.................................................................
def cartoonPage(request):
    cartoons = Cartoon.objects.order_by('-created_at')
    jerecan_size = Supplier.objects.all()
    if request.method == "POST":
        cartoon_company = request.POST['cartoon_company']
        cartoon_size = request.POST['cartoon_size']
        cartoon_price = request.POST['cartoon_price']
        cartoon = Cartoon(cartoon_company=cartoon_company,cartoon_price=cartoon_price,cartoon_size=cartoon_size)
        cartoon.save()
        messages.success(request , 'Cartoon Added Successfully')
        redirect('cartoonPage')
    return render(request , 'management/cartoonPage.html' , {'cartoons':cartoons , 'jerecan_size':jerecan_size})


def AddCartoonModal(request):
    return render(request , 'management/AddCartoon.html')

def add_cartoon_modal(request):
    cartoon_company = request.POST['cartoon_company']
    cartoon_size = request.POST['cartoon_size']
    cartoon_price = request.POST['cartoon_price']
    cartoon = Cartoon(cartoon_company=cartoon_company,cartoon_price=cartoon_price,cartoon_size=cartoon_size)
    cartoon.save()
    messages.success(request , 'Cartoon Added Successfully')
    return redirect('supplier')


def deleteCartoon(request , cr_id):
    cartoon = Cartoon.objects.get(id=cr_id)
    cartoon.delete()
    messages.success(request , 'Cartoon Deleted Successfully')
    return redirect('cartoonPage')

def cartoonInfo(request , cr_id):
    cartoon = Cartoon.objects.get(id=cr_id)
    return render(request , 'management/cartoon_info.html' , {'cartoon':cartoon})

def editCartoon(request , cr_id):
    cartoon = Cartoon.objects.get(id=cr_id)
    jerecan_size = Supplier.objects.all()
    return render(request , 'management/editCartoon.html' , {'cartoon':cartoon , 'jerecan_size':jerecan_size})


def updateCartoon(request , cr_id):
    cartoon = Cartoon.objects.get(id=cr_id)
    cartoon.cartoon_company = request.POST['cartoon_company']
    cartoon.cartoon_price = request.POST['cartoon_price']
    
    cartoon.save()
    messages.success(request , 'Cartoon Updated Successfully')
    return redirect('cartoonPage')


# Oil Suppliers Views.................................................................
def oilSupplierPage(request):
    oils = OilSupplier.objects.order_by('-created_at')
    jerecans = Supplier.objects.all()
    if request.method == "POST":
        oil_company = request.POST['oil_company']
        oil_name = request.POST['oil_name']
        oil_quantity = request.POST['oil_quantity']
        oil_price = request.POST['oil_price']
        oil_month_selling = request.POST['oil_month_selling']
        # jerecan_size = request.POST['jerecan_size']
    
        oil = OilSupplier(oil_company=oil_company,oil_name=oil_name, oil_quantity=oil_quantity,oil_price=oil_price,oil_month_selling=oil_month_selling)
        oil.save()
        messages.success(request , 'Oil Supplier Added Successfully')
        redirect('oilSupplierPage')
    return render(request , 'management/OilSuppliersPage.html' , {'oils':oils , 'jerecans':jerecans})

def addOilSuplierModal(request):
    return render(request , 'management/addOilSuplierModal.html')

def add_oil_suplier_modal(request):
    oil_company = request.POST['oil_company']
    oil_name = request.POST['oil_name']
    oil_quantity = request.POST['oil_quantity']
    oil_price = request.POST['oil_price']
    oil_month_selling = request.POST['oil_month_selling']
    oil = OilSupplier(oil_company=oil_company,oil_name=oil_name, oil_quantity=oil_quantity,oil_price=oil_price,oil_month_selling=oil_month_selling)
    oil.save()
    messages.success(request , 'Oil Supplier Added Successfully')
    return redirect('supplier')



def oilInfo(request , oi_id):
    oil = OilSupplier.objects.get(id=oi_id)
    return render(request , 'management/oilInfo.html' , {'oil':oil})

def deleteOilSupplier (request , oi_id):
    oil = OilSupplier.objects.get(id=oi_id)
    oil.delete()
    messages.success(request , 'Oil Supplier Deleted Successfully')
    return redirect('oilSupplierPage')

def editOilSupplier(request , oi_id):
    oil = OilSupplier.objects.get(id=oi_id)
    return render(request , 'management/editOilSupplier.html' , {'oil':oil})

def updateOilSupplier(request , oi_id):
    oil = OilSupplier.objects.get(id=oi_id)
    oil.oil_company = request.POST['oil_company']
    oil.oil_name = request.POST['oil_name']
    oil.oil_quantity = request.POST['oil_quantity']
    oil.oil_price = request.POST['oil_price']
    oil.oil_month_selling = request.POST['oil_month_selling']
    
    oil.save()
    messages.success(request , 'Oil Supplier Updated Successfully')
    return redirect('oilSupplierPage')


# Packging Processing and Loading Views.............................................
def packgingProcessing(request):
    shippings = ShippingDirection.objects.all()
    context={
        'shippings':shippings,
        
    }
    return render(request , 'management/packging_processing.html' , context)

def outPutPage(request , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    shippings = Shipping.objects.filter(direction__id=sh_id)
    
    context={
        'shippings':shippings,
        'direction':direction,
    }
    return render(request , 'management/outPutPage.html' , context)

def outPutPage_pdf(request , sh_id):
    direction = ShippingDirection.objects.get(id=sh_id)
    shippings = Shipping.objects.filter(direction__id=sh_id)
    context={
        'shippings':shippings,
        'direction':direction,
    }
    return render(request,'management/pdf.html')
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="Shipping_Report.pdf"'
    # template = get_template(template_path)
    # html = template.render(context)
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response)
    # # if error then show some funny view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    

# Certifications View..................................................................
def certificationPage(request):
    certifications = Certificate.objects.all()
    if request.method == "POST":
        certification_name = request.POST['certification_name']
        certification_price = request.POST['certification_price']
        certification_info = Certificate(cretificate_name=certification_name, cretificate_price=certification_price)
        certification_info.save()
        messages.success(request , 'certification Added Successfully')
        redirect('certificationPage')
    return render(request , 'management/certificationPage.html' , {'certifications':certifications})


def certificationDelete (request , ce_id):
    certification = Certificate.objects.get(id=ce_id)
    certification.delete()
    messages.success(request , 'Certification Deleted Successfully')
    return redirect('certificationPage')


def certificationEdit(request , ce_id):
    certification = Certificate.objects.get(id=ce_id)
    return render(request , 'management/certificationEdit.html' , {'certification':certification})

def certificattionInfo(request , ce_id):
    certification = Certificate.objects.get(id=ce_id)
    return render(request , 'management/certificationInfo.html' , {'certification':certification})

def certificattionUpdate(request , ce_id):
    certification = Certificate.objects.get(id=ce_id)
    certification.cretificate_name = request.POST['certificate_name']
    certification.cretificate_price = request.POST['certificate_price']
    certification.save()
    messages.success(request , 'Cretification Updated Successfully')
    return redirect('certificationPage')












def dataTable(request):
    return render(request , 'admin/dataTable.html')

def myProfile(request):
    return render(request  , 'admin/usersProfile.html')

def contactAdmin(request):
    return render(request , 'admin/admin_contact.html')

def userMessage(request):
    return render(request , 'admin/messages.html')
