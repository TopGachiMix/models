from django.db import models


class Advertisement(models.Model):
    title = models.CharField('заголовок',max_length=255)
    description = models.TextField('описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте,если торг уместен')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price:.2f})>'