from django import template
from WebBasicsExam.user_profile.models import Profile

register = template.Library()



@register.simple_tag()
def get_user_profile():
    return Profile.objects.first()
