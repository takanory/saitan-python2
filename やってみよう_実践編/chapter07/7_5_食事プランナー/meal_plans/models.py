from django.db import models

class Meal(models.Model):
    """ひとつの献立のモデル"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """献立の文字列表現を返す"""
        return self.name

class MealItem(models.Model):
    """献立の食材"""
    name = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """食材の文字列表現を返す"""
        return self.name 
