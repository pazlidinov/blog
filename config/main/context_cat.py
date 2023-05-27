from .models import Category


def main_context(request):
    all_categories = Category.objects.all()
    data = {
        'all_categories': all_categories,
    }
    return data
