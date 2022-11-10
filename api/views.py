from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .serializers import CodeSerializer
from base.models import CodeFile

import uuid

import json

@api_view(['GET'])
def allCodes(request):


    try:
        codes = CodeFile.objects.filter(user = request.user)
        serializer = CodeSerializer(codes, many = True)
    except Exception as e:
        print(e)
        serializer = {}

    return Response(serializer.data)

@api_view(['GET'])
def getCode(request, pk):

    code = CodeFile.objects.get(id = pk)
    serializer = CodeSerializer(code, many = False)

    return Response(serializer.data)

@api_view(['POST'])
def editCode(request, pk):

    code_obj = CodeFile.objects.get(id = pk)

    data_dumbed = json.dumps(request.data)
    data = json.loads(data_dumbed)

    code_obj.title = data['filename']
    code_obj.code = data['code']

    if data['scope'] != 'public':
        code_obj.private = True
    else:
        code_obj.private = False

    code_obj.save()

    return Response('Code updated')


@api_view(['POST'])
def addCode(request):

    try:
        user = request.user
        data_dumbed = json.dumps(request.data)
        data = json.loads(data_dumbed)

        filename = data['filename']
        code = data['code']
        print(data)

        code_file = CodeFile.objects.get_or_create(
            user = user,
            title = filename,
            code = code,
            link_id = str(uuid.uuid4())[:8],
        )

    except Exception as e:
        print(e)

    return Response('New code file added')


@api_view(['DELETE'])
def deleteCode(request, pk):

    try:
        user = request.user
        code = CodeFile.objects.get(user = user, id = pk)
        code.delete()

    except:
        pass
    return Response('Code deleted!')
