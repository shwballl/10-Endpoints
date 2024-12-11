from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Coffe
from .models import Category
from .models import Taste
from .models import FavCoffe
from .models import AlergensForCoffee
from .models import Stores
from .models import OrdersHistory
from .models import RewardsHistory
from .models import Specials


from .serializers import CoffeSerializer
from .serializers import CatSerializer
from .serializers import TasteSerializer
from .serializers import FavSerializer
from .serializers import AllergensSerializer
from .serializers import StoresSerializer
from .serializers import OrdersSerializer
from .serializers import RewardsSerializer
from .serializers import SpecialsSerializer


class CoffeAPIView(APIView):
	def get(self, request):
		lst = Coffe.objects.all()
		return Response({'menu': CoffeSerializer(lst, many=True).data})

	def post(self, request):

		serializer = CoffeSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		new_ = Coffe.objects.create(
			tittle = request.data['tittle'],
			content = request.data['content'],
			cat_id  = request.data['cat_id']
		)
		return Response({'status': 'ok', 'new item created:':CoffeSerializer(new_).data})

class CatAPIView(APIView):
	def get(self, request):
		lst = Category.objects.all()
		return Response({'categories': CatSerializer(lst, many=True).data})

	def post(self, request):
		serializer = CatSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		new_ = Category.objects.create(
			name = request.data['name'],
		)
		return Response({'status': 'ok', 'new item created:':CatSerializer(new_).data})


class TasteAPIView(APIView):
	def get(self, request):
		lst = Taste.objects.all()
		return Response({'tastes': TasteSerializer(lst, many=True).data})

class FavAPIView(APIView):
	def get(self, request):
		lst = FavCoffe.objects.all()
		return Response({'favourites': FavSerializer(lst, many=True).data})

class AllergensAPIView(APIView):
	def get(self, request):
		lst = AlergensForCoffee.objects.all()
		return Response({'allergens': AllergensSerializer(lst, many=True).data})

class StoresAPIView(APIView):
	def get(self, request):
		lst = Stores.objects.all()
		return Response({'stores': StoresSerializer(lst, many=True).data})

class OrdersHistoryAPIView(APIView):
	def get(self, request):
		lst = OrdersHistory.objects.all()
		return Response({'orders-history': OrdersSerializer(lst, many=True).data})

class RewardsHistoryAPIView(APIView):
	def get(self, request):
		lst = RewardsHistory.objects.all()
		return Response({'rewards-history': RewardsSerializer(lst, many=True).data})

class SpecialsAPIView(APIView):
	def get(self, request):
		lst = Specials.objects.all()
		return Response({'specials': SpecialsSerializer(lst, many=True).data})
