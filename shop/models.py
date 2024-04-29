from ckeditor.fields import RichTextField
from django.db import models
from django.forms import ValidationError


# Create your models here.
class Products(models.Model):

    def __self__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.DecimalField(max_digits=7,decimal_places=2)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    #in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

	
    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url

class Order_request(models.Model):
	customer = models.CharField(max_length=100)
	date_ordered = models.DateTimeField(auto_now_add=True)
	total = models.FloatField(max_length=15,null=True, blank=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=15, blank=True, null=True)
	items = models.CharField(max_length=255)
	order_total = models.CharField(max_length=15)
	
	def __str__(self):
		return str(self.customer)

	class Meta:
		verbose_name = "Order Request"
		verbose_name_plural = "Order Requests"

		
class Blog(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)
	content = RichTextField()
	category = models.CharField(max_length=30, default="sauce")
	publisher = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	views = models.IntegerField(default=0)
	tags = models.TextField()
	meta_description = models.TextField()
	meta_keywords = models.TextField()
	meta_title = models.TextField()
	

	def __str__(self):
		return self.title
	
	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
class About(models.Model):
	short_description = models.TextField()
	description = models.TextField()
	mission = models.TextField()
	image = models.ImageField(null=True, blank=True)
	about_the_company = models.TextField()
	about_the_company_image = models.ImageField(null=True, blank=True)
	meta_description = models.TextField()
	meta_keywords = models.TextField()
	meta_title = models.TextField()


	def __str__(self):
		return self.short_description
	
	def save(self, *args, **kwargs):
		if not self.pk and Footer.objects.exists():
			raise ValidationError('There can only be only one Footer')
		return super(About, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "About page"
		verbose_name_plural = "About Page"
	
	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	@property
	def Imageurl(self):
		try:
			url = self.about_the_company_image.url
		except:
			url = ''
		return url

class Footer(models.Model):
	short_company_description = models.TextField(max_length=40)
	email = models.CharField(max_length=60)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=40)
	footer_logo_image = models.ImageField(null=True, blank=True)
	facebook_link = models.CharField(max_length=250)
	instagram_link = models.CharField(max_length=250)
	linkedn_link = models.CharField(max_length=250)

	def save(self, *args, **kwargs):
		if not self.pk and Footer.objects.exists():
			raise ValidationError('There can only be only one Footer')
		return super(Footer, self).save(*args, **kwargs)

	def __str__(self):
		return self.short_company_description
	
	@property
	def ImageURL(self):
		try:
			url = self.footer_logo_image.url
		except:
			url = ''
		return url

	class Meta:
		verbose_name = "Footer"
		verbose_name_plural = "Footer"

class Team(models.Model):
	name = models.TextField(max_length=40)
	position = models.CharField(max_length=60)
	description = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)	

	def __str__(self):
		return self.name
	
	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	class Meta:
		verbose_name = "Team member"
		verbose_name_plural = "Team"

class Home(models.Model):
	welcome_text = models.TextField()
	subtext = models.TextField()
	welcome_image = models.ImageField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	company_description_title = models.TextField()
	company_description = models.TextField()
	meta_description = models.TextField()
	meta_keywords = models.TextField()
	meta_title = models.TextField()



	def __str__(self):
		return self.welcome_text
	
	def save(self, *args, **kwargs):
		if not self.pk and Home.objects.exists():
			raise ValidationError('There can only be only one Home')
		return super(Home, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "Home page"
		verbose_name_plural = "Home Page"
	
	@property
	def ImageURL(self):
		try:
			url = self.welcome_image.url
		except:
			url = ''
		return url
	@property
	def ImageUrl(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class Testimonial(models.Model):
	name = models.CharField(max_length=60)
	testimony = models.CharField(max_length=260)
	stars = models.IntegerField()
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def ImageURL(self):
		try:
			url = self.image
		except:
			url = ''
		return url

class Subscriber(models.Model):
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.email

class Contact(models.Model):
	big_text = models.CharField(max_length=40)
	subtext = models.CharField(max_length=40)
	image = models.ImageField(null=True, blank=True)
	address = models.CharField(max_length=70)
	email = models.CharField(max_length=70)
	phone = models.CharField(max_length=15)



	def __str__(self):
		return self.big_text
	
	def save(self, *args, **kwargs):
		if not self.pk and Contact.objects.exists():
			raise ValidationError('There can only be only one Contact page')
		return super(Contact, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "Contact page"
		verbose_name_plural = "Contact Page"
	
	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Message(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	message = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name

class Product_page(models.Model):
	big_text = models.CharField(max_length=150)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.big_text

	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def save(self, *args, **kwargs):
		if not self.pk and Product_page.objects.exists():
			raise ValidationError('There can only be only one Products page')
		return super(Product_page, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "Products page"
		verbose_name_plural = "Products page"

class Blogs_page(models.Model):
	big_text = models.CharField(max_length=30)
	subtext = models.CharField(max_length=150)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.big_text

	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def save(self, *args, **kwargs):
		if not self.pk and Blogs_page.objects.exists():
			raise ValidationError('There can only be only one Blogs page')
		return super(Blogs_page, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "Blogs page"
		verbose_name_plural = "Blogs page"

class Subscription_image(models.Model):
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.id)

	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def save(self, *args, **kwargs):
		if not self.pk and Subscription_image.objects.exists():
			raise ValidationError('There can only be only one Subscription image')
		return super(Subscription_image, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name = "Subscription image"
		verbose_name_plural = "Subscription image"

class Partner(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def ImageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url