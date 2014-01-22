from .models import MenuItem


def menu(request):
    """
    Example return:

        [index,
            (lev1.1, [lev2.1.1, lev2.1.2, lev2.1.3]),
            (lev1.2, [lev2.2.1, lev2.2.2]),
            (lev1.3, [])
        ]

    Output structure:

        index
         |
         +- lev1.1
         |   |
         |   +- lev2.1.1
         |   +- lev2.1.2
         |   +- lev2.1.3
         |
         +- lev1.2
         |   |
         |   +- lev2.2.1
         |   +- lev2.3.2
         |
         +- lev1.3

    :return: menu items structure
    :rtype: list
    """

    active_menu_items = MenuItem.objects.filter(is_active=True)
    index = active_menu_items.get(parent__isnull=True)
    menu_list = [index, []]

    for level1 in active_menu_items.filter(parent=index):
        menu_list[1].append(
            (level1, active_menu_items.filter(parent=level1))
        )

    return {'menu': menu_list}
