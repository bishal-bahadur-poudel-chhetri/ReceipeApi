# from django.db import models
# import uuid,random

# from django.contrib.auth import get_user_model
# User=get_user_model()

# class BaseModel(models.Model):
#     update_at=models.DateField(auto_now=True)
#     created_at=models.DateField(auto_now=True)
#     class Meta:
#         abstract=True

# class ReceipeCategory(BaseModel):
#     category_id=models.AutoField(primary_key=True)
#     category_name=models.TextField(max_length=15)
#     def __str__(self):
#         return self.category_name

# # Create your models here.
# class Receipe(models.Model):
#     receipe_id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
#     receipe_title=models.CharField(max_length=15)
#     receipe_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     category_id=models.ForeignKey(ReceipeCategory,on_delete=models.CASCADE,related_name="receipe_category")
#     Description=models.TextField()
#     Prep_time=models.DecimalField(max_digits=5,decimal_places=1)
#     cook_time=models.DecimalField(max_digits=5,decimal_places=1)
#     serving_quantity=models.IntegerField(2)
#     categoryImage=models.ImageField(null=True, blank=True)
#     def __str__(self):
#         return self.receipe_title
    

    


# class ReceipeIngredient(models.Model):
#     receipe_id=models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="receipe_identity")
#     ingredient_id=models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="receipe_identity")
#     amount=models.IntegerField(20,default=1)
#     unit=models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="receipe_identity")

#     def __str__(self):
#         return self.receipe_id

# class Ingredient(models.Model):
#     ingredient_id=models.AutoField(primary_key=True)
#     ingredient_name=models.CharField(max_length=15)
#     def __str__(self):
#         return self.ingredient_name
    
# class Unit(models.Model):
#     unit_id=models.AutoField(primary_key=True)
#     unit_name=models.CharField(max_length=5)
#     def __str__(self):
#         return self.unit_id
    
# class Review(BaseModel):
#     review_id=models.AutoField(primary_key=True)
#     receipe_id=models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="review_identity")
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     comment=models.CharField(max_length=30)

#     def __str__(self):
#         return self.unit_id