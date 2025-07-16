from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from .userSerializer import UserSerializer , LoginSerializer
from rest_framework.response import Response
import jwt


#FBV
@api_view(["POST"])
def login(request):
    serializerData = LoginSerializer(data=request.data)

    if serializerData.is_valid():
        clientuserdata = serializerData.validated_data

        try:
            realuserdata = User.objects.get(userName=clientuserdata["username"])
            realuserdata = UserSerializer(realuserdata).data

            payload={
                "userId":clientuserdata["username"]
            }
            token=jwt.encode(payload, "secrect-key")

            if realuserdata["password"] == clientuserdata["password"]:
                print(clientuserdata)
                return Response(data={
                    "msg":"welcome",
                    "token": token,
                })
            else:
                return Response({
                    "msg": "Invalid Username/Password"
                })

        except:
            return Response({
                "msg": "Invalid Username/Password"
            })

    return Response(serializerData.errors)

@api_view(["POST"])
def register(request):
    serializerData = UserSerializer(data=request.data)

    if serializerData.is_valid():
        serializerData.save()
        return Response({
            "msg": "User Registered Successfully","userData" : serializerData .data
        })
    else:
        return Response(serializerData.errors)