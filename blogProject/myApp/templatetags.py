from Django import template
from myApp.models import Post
register=template.Library()
@register.simple_tag
def total_posts():
	return Post.objects.count()
@register.inclusion_tag('myApp/latest_post.html')
def show_latest_post(count=3):
	latest_posts=Podt.objects.orderby('-publish')[:count]