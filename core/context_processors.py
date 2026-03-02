from core.models import Menu


def menu_context(request):
    menu_items = (
        Menu.objects.filter(parent__isnull=True, is_active=True)
        .prefetch_related('children')
        .order_by('order', 'id')
    )
    return {'menu_items': menu_items}