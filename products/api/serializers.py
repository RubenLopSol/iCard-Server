from rest_framework.serializers import ModelSerializer

from products.models import Product
from categories.api.serializers import CategorySerializer




class ProductSerializer(ModelSerializer):

    #Para poder ver los datos de la categoria, al vicualizar los productos ('populate')
    category_data = CategorySerializer(source= 'category', read_only= True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'price', 'active', 'category', 'category_data']