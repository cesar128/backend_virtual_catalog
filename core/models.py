from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Item(models.Model):

    name = models.CharField("Nombre delarticulo", max_length=50)
    description = models.TextField(_("Descripcion del articulo"))
    show = models.BooleanField(_("Mostrar?"))
    piture = models.FileField(_("Imagen principal"))

    class Meta:
        verbose_name = _("Articulo")
        verbose_name_plural = _("Articulos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})


class ItemPicture(models.Model):

    class Meta:
        verbose_name = _("itempicture")
        verbose_name_plural = _("itempictures")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itempicture_detail", kwargs={"pk": self.pk})
