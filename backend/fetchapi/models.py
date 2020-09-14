from django.db import models

class table1(models.Model):
    _id = models.CharField(max_length=100,blank=True,null=True)
    oem_id = models.CharField(max_length=100,blank=True,null=True)
    oem_name = models.CharField(max_length=100,blank=True,null=True)
    oem_type = models.CharField(max_length=100,blank=True,null=True)
    oem_logo = models.CharField(max_length=100,blank=True,null=True)
    _class = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.id)

class contact_info(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    sur_name = models.CharField(max_length=100,blank=True,null=True)
    family_name = models.CharField(max_length=100,blank=True,null=True)
    contact_type = models.CharField(max_length=100,blank=True,null=True)
    mobile_no = models.CharField(max_length=100,blank=True,null=True)
    alternate_no = models.CharField(max_length=100,blank=True,null=True)
    landline_no = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    emp_id = models.CharField(max_length=100,blank=True,null=True)
    owner = models.ForeignKey(table1,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.id)

class oem_corp_address(models.Model):
    house_no = models.CharField(max_length=100,blank=True,null=True)
    flat_name = models.CharField(max_length=100,blank=True,null=True)
    building_no = models.CharField(max_length=100,blank=True,null=True)
    address_line = models.CharField(max_length=100,blank=True,null=True)
    street = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    landmark = models.CharField(max_length=100,blank=True,null=True)
    owner = models.ForeignKey(table1,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.id)


