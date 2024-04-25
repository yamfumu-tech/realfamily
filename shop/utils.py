from .models import Blog, Products

def get_most_viewed_blog_post():
    # Query all the blog posts
    all_blog_posts = Blog.objects.all()

    # Initialize variables to track the most viewed blog post
    most_viewed_post = None
    max_views = 0

    # Iterate over the queryset and find the blog post with the most views
    for post in all_blog_posts:
        if post.views > max_views:
            max_views = post.views
            most_viewed_post = post

    return most_viewed_post

def get_product_categories():
    # Query for distinct categories
    categories = Products.objects.values_list('category', flat=True).distinct()
    return categories