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
    index = MenuItem.objects.get(parent__isnull=True, is_active=True)

    menu_list = [index, []]

    for level1 in index.children.filter(is_active=True):
        menu_list[1].append(
            (level1, list(level1.children.filter(is_active=True)))
        )

    return {'menu': menu_list}
