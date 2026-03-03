from core.models import Menu, TopbarSettings


def menu_context(request):
    menu_items = (
        Menu.objects.filter(parent__isnull=True, is_active=True)
        .prefetch_related('children')
        .order_by('order', 'id')
    )
    topbar = TopbarSettings.objects.filter(is_active=True).first()
    return {
        'menu_items': menu_items,
        'topbar_settings': topbar,
    }
