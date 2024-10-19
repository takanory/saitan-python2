from django.db import models

class Pizza(models.Model):
    """ピザ屋で注文できるピザの種類を表す"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name

class Topping(models.Model):
    """ピザに乗せられるトッピング"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name