from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     follows = models.ManyToManyField("self", related_name="follwed_by" , symmetrical=False , blank=True )
#     created_at = models.DateTimeField(User , auto_now=True)

# Create Profile Model............
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    followes = models.ManyToManyField("self" , related_name="followed_by" , symmetrical=False , blank=True)
    date_modification = models.DateTimeField(User , auto_now=True)
    def __str__(self):
        return self.user.username
    
# Create profile when user is created...............
def create_Profil(sender , instance , created , **Kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        user_profile.followes.set([instance.profile.id])
        user_profile.save()
post_save.connect(create_Profil , sender=User)



# Create Twieet Model....................
class Twieet(models.Model):
    user = models.ForeignKey(User , related_name="Twieets" , on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(
            f"{self.user}"
            f"{self.body}...."
            f"{self.created_at:%Y-%M-%D-%H-%M-%S}"
        )
    

# Create Certificate Model...........................
class Certificate(models.Model):
    cretificate_name = models.CharField(max_length=50)
    cretificate_price = models.DecimalField(max_digits=10 , max_length=8 , decimal_places=4)


#Create ShippingDirection Model........................
class ShippingDirection(models.Model):
    direction = models.CharField(max_length=100)

    def __str__(self):
        return(
            f"{self.direction}"
        )
    
    # Create Sticker Model.......................
class Sticker(models.Model):
    sticker_company = models.CharField(max_length=100)
    sticker_size = models.DecimalField(max_digits=10 , max_length=6 , decimal_places=3)
    sticker_price = models.DecimalField(max_digits=10 , max_length=6 , decimal_places=3)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(
            f"{self.sticker_company}"
            f"{self.sticker_size}"
            f"{self.sticker_price}"
            f"{self.created_at}"
        )

    
# Create Oil Supplier Model.......................
class OilSupplier(models.Model):
    oil_company = models.CharField(max_length=100)
    oil_name = models.CharField(max_length=50)
    oil_quantity = models.DecimalField(max_digits=10 , max_length=10 , decimal_places=5)
    oil_price = models.DecimalField(max_digits=10 , max_length=10 , decimal_places=5)
    oil_month_selling = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def net_price(self):
        return (float(self.oil_price)/(1000/(float(self.supplier_set.first().jon_size)*0.9)))

    def __str__(self):
        return(
            f"{self.oil_company}"
            f"{self.oil_name}"
            f"{self.oil_quantity}"
            f"{self.oil_price}"
            f"{self.oil_month_selling}"
            f"{self.created_at}"
        )


# Create Cartoon Model.......................
class Cartoon(models.Model):
    cartoon_company = models.CharField(max_length=100)
    cartoon_size = models.DecimalField(max_digits=10 , max_length=8, decimal_places=4)
    cartoon_price = models.DecimalField(max_digits=10 , max_length=8, decimal_places=4)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(
            f"{self.cartoon_company}"
            f"{self.jearecane}"
            f"{self.cartoon_size}"
            f"{self.cartoon_price}"
            f"{self.created_at}"
        )



# Create Supplier Model.......................
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    jon_size = models.DecimalField(max_digits=10 , max_length=8 , decimal_places=4)
    jon_count = models.BigIntegerField(null=True)
    value_ofTonToLiter = models.BigIntegerField(null=True)
    jerecan_sticker = models.ForeignKey(Sticker , on_delete=models.CASCADE , null=True)
    cartoon = models.ForeignKey(Cartoon , on_delete=models.CASCADE , null=True)
    jerecan_oil = models.ForeignKey(OilSupplier , on_delete=models.CASCADE , null=True)
    joi_price = models.DecimalField(max_digits=10 , max_length=8 , decimal_places=4)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def loadding(self):
        return((float(self.jon_size)*float(self.jon_count)*0.9)/1000*(self.value_ofTonToLiter + 6)/float(self.jon_count))

    def __str__(self):
        return(
            f"{self.supplier_name}"
            f"{self.jon_size}"
            f"{self.joi_price}"
            f"{self.created_at}"
        )


# Create Shipping Model...........................
class Shipping(models.Model):
    
    company_name = models.CharField(max_length=150)
    direction = models.ForeignKey(ShippingDirection , on_delete=models.CASCADE ,related_name="shippings", null=True)
    jerecan = models.ForeignKey(Supplier , on_delete=models.CASCADE , null=True)
    trip_Price = models.DecimalField(max_digits=10 , max_length=10 , decimal_places=5)
    trip_date = models.CharField(max_length=100)
    trip_Time = models.CharField(max_length=100)
    grossing = models.DecimalField(max_digits=10 , max_length=10 , decimal_places=5 , default=3)
    margin = models.DecimalField(max_digits=10 , max_length=10 , decimal_places=5 , default=1.5)
    certification = models.ForeignKey(Certificate , on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def total_price_units(self):
        # if self.jerecan.jerecan_oil.first() != None:
        net_price = self.jerecan.jerecan_oil.net_price
        return(float(self.jerecan.joi_price)+float(self.jerecan.jerecan_sticker.sticker_price)+float(self.jerecan.cartoon.cartoon_price)+
               float(self.jerecan.loadding)+float(self.certification.cretificate_price)/1320+net_price/4.64+float(self.grossing)+float(self.margin))

    @property
    def fixed(self):
        return(1000/(float(self.jerecan.jon_size)*0.9)*self.total_price_units)


    def __str__(self):
        return(
            f"{self.company_name}"
            f"{self.trip_Price}"
            f"{self.trip_date}"
            f"{self.trip_Time}"
            f"{self.created_at}"
        )
    

    





