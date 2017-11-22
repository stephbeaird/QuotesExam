from __future__ import unicode_literals
from django.db import models
import datetime
from django.core.validators import validate_email
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['name']) < 2:
            errors.append("Name must be 2 or more characters.")
            # session['name'] = Name['name']
        
        if len(postData['alias']) < 2:
            errors.append("Alias must be 2 or more characters.")
            # session['alias'] = Alias['alias']
        
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors.append("Email is not valid.")
        
        if len(postData['password']) < 8 or len(postData['confirm_password']) < 8:
            errors.append("Password must be 8 or more characters.")
        
        if postData['password'] != postData['confirm_password']:
            errors.append("Passwords must match.")
        
        try:
            User.object.get(email=postData['email'])
            errors.append("Email already taken.")
        except:
            pass
        
        try:
            print postData['email']
            validate_email(postData['email'])
        except Exception as e:
            print e
            errors.append("Email must be in valid format.")
        else:
            print("Email worked!")
        
        if errors:
            return {'err_messages': errors}
    
        else:
            hash_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(Name = postData['name'], Alias = postData['alias'], Email = postData['email'], Password = hash_pw)        
            return {'new_user': user}
        
        # try:
        #     validate_password(postData['password'])
        # except ValidationError as e:
        #     errors.append("Password must match!")
        # else:
        #     print("Password worked!")

    def login(self, postData):
        try:
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                return {'logged_user': user}
            else:
                return {'err_messages': ['Email/Password invalid. Please try again.']}
        except:
            return {'err_messages': ['Email does not exist. Please register']}


class Users(models.Model):
    Name = models.CharField(max_length = 255)
    Alias = models.CharField(max_length = 255)
    Email = models.CharField(max_length = 255)
    Password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class List(models.Model):
    Quote = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Contribute(models.Model):
    Author = models.CharField(max_length = 255)
    Message = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def contribute(self, postData):
    #     try:
    #         User.object.post(quote=postData['quote'])
    #         errors.append("Email already taken.")

# def validator(self, postData):
#     errors = []
#     if len(postData['name']) < 2:
#     errors.append("Name must be 2 or more characters.")
    
    # objects = QuoteMaker()

    # def remove_from_list(self, postData):
    #     errors = []
    #     print(postData)

    #     if len(postData['Quote'])