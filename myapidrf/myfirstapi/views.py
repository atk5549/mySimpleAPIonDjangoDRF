import os
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from wsgiref.util import FileWrapper
from rest_framework import generics


class CreateMyXMLFile(APIView):

    def get(self, request):
        data = {
            'filename': 'anyfilename',
            'extends': 'anyextends',
            'datainfile': 'anydataforfile'
        }
        return Response(data)



    def post(self, request):
        # получаем значение ключей
        filename = request.data.get("filename")
        extends = request.data.get("extends")
        datainfile = request.data.get("datainfile")
        print(datainfile)

        # отдаем в ответе значение ключа some
        data = {
            'filename': f'{filename}',
            'extends': f'{extends}',
            'datainfile': f'{datainfile}'
        }

        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f"\\media\\"
        # генерируется xml-файл с именем переданным в переменную user_id_token
        with open(os.path.join(path, f"{filename}.{extends}"), 'w', encoding="utf-8") as fp:
            fp.write(f'{str(datainfile)}')
            fp.close()

    def download(self, request):
        path_and_filname = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f"\\media\\crewlist.html"
        if os.path.exists(path_and_filname):
            img = open(path_and_filname, 'rb')
            response = FileResponse(img)
            response['Content-Disposition'] = f"Attachment;filename={os.path.basename(path_and_filname)}"
            return response


