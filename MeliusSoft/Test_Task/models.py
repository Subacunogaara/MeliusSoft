from django.db import models


class CreditApplicationModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    date_of_creation = models.DateField(auto_now_add=True)
    contract = models.ForeignKey('ContractModel', on_delete=models.PROTECT, null=True,
                                 verbose_name='Контракт', related_name='contract_entries')

    class Meta:
        verbose_name = 'Кредитная заявка'
        verbose_name_plural = 'Кредитные заявки'

    def __str__(self):
        return self.title



class ContractModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    date_of_creation = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return self.title



class ProductModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    date_of_creation = models.DateField(auto_now_add=True)
    credit_application =models.ForeignKey(CreditApplicationModel, on_delete=models.PROTECT, null=True,
                                          related_name='credit_entries', verbose_name='Кредитная заявка')
    manufacturer = models.ForeignKey('ManufacturerModel', on_delete=models.PROTECT, null=True,
                                     verbose_name='Производитель', related_name='manufacturer_entries')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title



class ManufacturerModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    date_of_creation = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.title
