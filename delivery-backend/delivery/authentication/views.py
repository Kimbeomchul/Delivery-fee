import requests

from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from json.decoder import JSONDecodeError

from rest_framework import status
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from users.models import User


BASE_URL = 'http://localhost:8000/api/v1/auth'

GOOGLE_CALLBACK_URI = BASE_URL + '/google/callback/'
KAKAO_CALLBACK_URI = BASE_URL + '/kakao/callback/'

KAKAO_REST_API_KEY = '132e6e56a442ec9fa1decbcfadd50cfb'
GOOGLE_CLIENT_ID = "420742298215-p0m9b01clio90n5t3e9el83kjjqotuhq.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"

state = "random_string"


def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    
    google_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}"
    
    return JsonResponse({'url': google_url}, status=status.HTTP_200_OK)


def google_callback(request):
    code = request.GET.get('code')
    
    # googleapis를 이용하기 위한 access_token을 얻는 OAuth request
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={GOOGLE_CLIENT_ID}&client_secret={GOOGLE_CLIENT_SECRET}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}"
    )
    token_req_json = token_req.json()

    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_req_json.get('access_token')

    # 사용자 정보 request
    profile_request = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}"
    )

    if profile_request.status_code != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    
    profile_json = profile_request.json()
    email = profile_json.get('email')
    
    
    # SignUp OR SignIn
    # dj_rest_auth를 통해 가입 처리
    data = {'access_token': access_token, 'code': code}
    finish_response = requests.post(
        f"{BASE_URL}/google/login/finish/", data=data)
    finish_status = finish_response.status_code
    
    if finish_status != 200:
        return JsonResponse({'err_msg': 'failed to google login'}, status=finish_status)

    finish_json = finish_response.json()

    access_token = finish_json['access_token']
    refresh_token = finish_json['access_token']
    user_id = finish_json['user']['pk']
    nickname = User.objects.get(id=user_id).nickname
        
    return redirect(f"http://localhost:8080/list/?access_token={access_token}&refresh_token={refresh_token}&user_id={user_id}&nickname={nickname}")


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


def kakao_login(request):
    kakao_url = f"https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_REST_API_KEY}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"

    return JsonResponse({'url': kakao_url}, status=status.HTTP_200_OK)

def kakao_callback(request):
    code = request.GET.get("code")
    redirect_uri = KAKAO_CALLBACK_URI

    # kapi를 이용하기 위한 access_token을 얻는 OAuth request
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_REST_API_KEY}&redirect_uri={redirect_uri}&code={code}"
    )
    token_req_json = token_req.json()

    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_req_json.get("access_token")

    # 사용자 정보 request
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    profile_json = profile_request.json()

    error = profile_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)

    kakao_account = profile_json.get('kakao_account')
    email = kakao_account.get('email')

    # SignUp OR SignIn
    # dj_rest_auth를 통해 가입 처리
    data = {'access_token': access_token, 'code': code}
    finish_response = requests.post(f"{BASE_URL}/kakao/login/finish/", data=data)
    finish_status = finish_response.status_code

    if finish_status != 200:
        return JsonResponse({'err_msg': 'failed to kakao login'}, status=finish_status)

    finish_json = finish_response.json()

    access_token = finish_json['access_token']
    refresh_token = finish_json['access_token']
    user_id = finish_json['user']['pk']
    nickname = User.objects.get(id=user_id).nickname

    return redirect(f"http://localhost:8080/list/?access_token={access_token}&refresh_token={refresh_token}&user_id={user_id}&nickname={nickname}")


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI
