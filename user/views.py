#비밀번호 변경하는 기능 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required #forms.py 파일 따로 안만들고 
from django.contrib.auth import update_session_auth_hash

@login_required #로그인 상태여야함상태여야함
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션의 인증 정보 업데이트
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


#이전기록 가져오는 기능
from apply.models import Application

def user_history(request):
    # 현재 로그인한 사용자의 이전 지원 기록을 가져옵니다.
    history = Application.objects.filter(user=request.user)
    
    return render(request, 'user_history.html', {'history': history})