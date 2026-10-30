
from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content
    
class Userprofile(models.Model):
    userprofile_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    bio = models.TextField(null=True, blank=True)
    VISIBILITY_CHOICES = [
            ('public', 'Public'),
            ('private', 'Private'),
            
        ]
    visibility = models.CharField(
            max_length=10,
            choices=VISIBILITY_CHOICES,
            default='pending'
        )
    
    class Meta:
        db_table = 'userprofile'

    def __str__(self):
        return f"Profile of {self.user.name}"
    
class Tag (models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    TAG_CHOICES = [
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('business', 'Business'),
        ('other', 'Other')]
    
    tag_type = models.CharField(max_length=50,
                                
        choices=TAG_CHOICES,
         default='programming'
        )
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Tag'

    def __str__(self):
        return self.name
    
class PostTag(models.Model):
    post_tag_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'post_tag'
    def __str__(self):
        return f"Tag {self.tag.name} for Post {self.post.title}"
    
class PostLike(models.Model):
    post_like_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'post_like'
    def __str__(self):
        return f"Like for Post {self.post.title} by User {self.user.username}"