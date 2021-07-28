import ast
import json
import base64

import json
from random import randint
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.http import Http404
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.generics import GenericAPIView
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.db.models import Q
from openpyxl import Workbook
from django.db.models import Sum
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .serializers import *
# Create your views here.
from .models import *
				
from rest_framework import generics
from .schema import *

from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import FormParser, MultiPartParser

from simpleproject.task import *



class fileList(APIView):
	"""
	List all categories, or create a new company.
	"""

	

	schema = fileSchema()
	parser_classes = (FormParser, MultiPartParser)

	def get(self, request, format=None):
		obj = file.objects.all()
		serializer = fileSerializer(obj, many=True)
		return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)

	
	def post(self, request, format=None):
		print(request.data)

		serializer = fileSerializer(data = request.data)
		print("hi")
		if serializer.is_valid():
			data  = serializer.save()
			print("data.id",data.id)

			my_first_task.delay(20)
			return JsonResponse({'success':True,"data":"done"}, status=status.HTTP_201_CREATED)
		return JsonResponse({'success':False,"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class fileDetail(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	# permission_classes = [IsAllowedToWrite]
	schema = fileSchema()

	def get_object(self, id):
		try:
			return file.objects.get(id=id)
		except file.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		obj = self.get_object(id)
		serializer = fileSerializer(obj)
		return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)

	def put(self, request, id, format=None):
		obj = self.get_object(id)
		serializer = fileSerializer(obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)
		return Response({'success':False,"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		obj = self.get_object(id)
		obj.delete()
		return Response({'success':True,"data":"Delete successfully"},status=status.HTTP_204_NO_CONTENT)


class SimpleList(APIView):
	"""
	List all categories, or create a new company.
	"""

	

	# schema = SimpleSchema()

	def get(self, request, format=None):
		obj = Simple.objects.all()
		serializer = SimpleSerializer(obj, many=True)
		return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)

	
	def post(self, request, format=None):
		serializer = SimpleSerializer(data = request.data)
		if serializer.is_valid():
			data  = serializer.save()
			return Response({'success':True,"data":serializer.data}, status=status.HTTP_201_CREATED)
		return Response({'success':False,"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SimpleDetail(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	# permission_classes = [IsAllowedToWrite]
	# schema = SimpleSchema()

	def get_object(self, id):
		try:
			return Simple.objects.get(id=id)
		except Simple.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		obj = self.get_object(id)
		serializer = SimpleSerializer(obj)
		return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)

	def put(self, request, id, format=None):
		obj = self.get_object(id)
		serializer = SimpleSerializer(obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'success':True,"data":serializer.data},status=status.HTTP_200_OK)
		return Response({'success':False,"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		obj = self.get_object(id)
		obj.delete()
		return Response({'success':True,"data":"Delete successfully"},status=status.HTTP_204_NO_CONTENT)



def task():
	file_ins = file.objects.filter(status = False)
	print("HI")
	for i in file_ins:
		try:
			with open(i.field_name.path, 'r') as file1:
				reader = csv.reader(file1)
				position = 0

				for row in reader:


					if position == 1:
						try:

							data = Simple.objects.create(GenderFreeForm =row[0],
							KaggleMotivationFreeForm =row[1],
							CurrentJobTitleFreeForm =row[2],
							MLToolNextYearFreeForm =row[3],
							MLMethodNextYearFreeForm =row[4],
							LanguageRecommendationFreeForm =row[5],
							PublicDatasetsFreeForm =row[6],
							PersonalProjectsChallengeFreeForm =row[7],
							LearningPlatformCommunityFreeForm =row[8],
							LearningPlatformFreeForm1 =row[9],
							LearningPlatformFreeForm2 =row[10],
							LearningPlatformFreeForm3 =row[11],
							LearningPlatformUsefulnessCommunitiesFreeForm =row[12],
							LearningPlatformUsefulnessFreeForm1Select =row[13],
							LearningPlatformUsefulnessFreeForm1SelectFreeForm =row[14],
							LearningPlatformUsefulnessFreeForm2Select =row[15],
							LearningPlatformUsefulnessFreeForm2SelectFreeForm =row[16],
							LearningPlatformUsefulnessFreeForm3Select =row[17],
							LearningPlatformUsefulnessFreeForm3SelectFreeForm =row[18],
							BlogsPodcastsNewslettersFreeForm =row[19],
							JobSkillImportanceOtherSelect1FreeForm =row[20],
							JobSkillImportanceOtherSelect2FreeForm =row[21],
							JobSkillImportanceOtherSelect3FreeForm =row[22],
							CoursePlatformFreeForm =row[23],
							HardwarePersonalProjectsFreeForm =row[24],
							ProveKnowledgeFreeForm =row[25],
							ImpactfulAlgorithmFreeForm =row[26],
							InterestingProblemFreeForm =row[27],
							DataScienceIdentityFreeForm =row[28],
							MajorFreeForm =row[29],
							PastJobTitlesFreeForm =row[30],
							FirstTrainingFreeForm =row[31],
							LearningCategoryOtherFreeForm =row[32],
							MLSkillsFreeForm =row[33],
							MLTechniquesFreeform =row[34],
							EmployerIndustryOtherFreeForm =row[35],
							EmployerSearchMethodOtherFreeForm =row[36],
							JobFunctionFreeForm =row[37],
							WorkHardwareFreeForm =row[38],
							WorkDataTypeFreeForm =row[39],
							WorkLibrariesFreeForm =row[40],
							WorkAlgorithmsFreeForm =row[41],
							WorkToolsFreeForm1 =row[42],
							WorkToolsFreeForm2 =row[43],
							WorkToolsFreeForm3 =row[44],
							WorkToolsFrequencySelect1FreeForm =row[45],
							WorkFrequencySelect2FreeForm =row[46],
							WorkFrequencySelect3FreeForm =row[47],
							WorkMethodsFreeForm1 =row[48],
							WorkMethodsFreeForm2 =row[49],
							WorkMethodsFreeForm3 =row[50],
							WorkMethodsFrequencySelect1FreeForm =row[51],
							WorkMethodsFrequencySelect2FreeForm =row[52],
							WorkMethodsFrequencySelect3FreeForm =row[53],
							TimeOtherSelectFreeForm =row[54],
							WorkChallengesFreeForm =row[55],
							WorkChallengeFrequencyOtherFreeForm =row[56],
							WorkMLTeamSeatFreeForm =row[57],
							WorkDataStorageFreeForm =row[58],
							WorkCodeSharingFreeForm =row[59],
							SalaryChangeFreeForm =row[60],
							JobSearchResourceFreeForm =row[61]
							)
							print(data.id)
						except:
							pass
					else:
						position =1
			print("done")
			file.objects.filter(id =i["id"]).update(status = True)
			print("done")
			return True
		except:
			return True



@csrf_exempt
def my_task(duration):
    print(duration)
    url_meeting = requests.post("http://127.0.0.1:8000/hi")
    print(url_meeting)
    
    return('first_task_done')