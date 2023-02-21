from django.db import models


class Menu(models.Model):
    menu_name = models.CharField('Menu', max_length=50)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.menu_name


class MenuItem(models.Model):
    item_name = models.CharField('Menu item', max_length=50)
    item_url = models.SlugField('URL menu item', max_length=50, unique=True)
    main_menu = models.ForeignKey(
        Menu, verbose_name='Main Menu', on_delete=models.CASCADE
    )
    parent_item = models.ForeignKey(
        to='self', verbose_name='Parent menu item',
        blank=True, null=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.item_name
