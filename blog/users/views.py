from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog import settings
from users.forms import UserUpdateForm, PictureUpdateForm, PasswordChange
from articles.forms import ArticlesForm

user = get_user_model()

""" CREATE ARTICLE """


@login_required()
def dashboard(request):
    context = {
        'title': f'{settings.PLATFORM_NAME} | Dashboard',
        'form': ArticlesForm()
    }
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'Successfully saved article')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Please check your details and submit again')
            return redirect('dashboard')
    return redirect(request, 'users/dashboard.html', context=context)


""" ACCOUNT VIEW """


@login_required()
def account(request):
    context = {
        'title': f'{settings.PLATFORM_NAME} | Account',
        'user_update_form': UserUpdateForm(instance=request.user),
        'picture_update_form': PictureUpdateForm(request.FILES, instance=request.user)
    }
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        picture = PictureUpdateForm(request.FILES, request.POST, instance=request.user)
        if form.is_valid() and picture.is_valid():
            form.save()
            picture.save()
            messages.success(request, 'Successfully updated account details')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Check you details')
            return redirect('account')
    return render(request, 'users/account.html', context=context)


""" CHANGE PASSWORD """


@login_required()
def change_password(request):
    context = {
        'title': f'{settings.PLATFORM_NAME} | Change Password',
        'header': 'Change Password',
        'form': PasswordChange(user=request.user)
    }
    if request.method == 'POST':
        old = request.POST.get('old_password')
        new1 = request.POST.get('new_password1')
        new2 = request.POST.get('new_password2')

        if authenticate(request, username=request.user.username, password=old):
            if new1 != new2:
                messages.warning(request, "Passwords Don't Match")
                return redirect('change-password')
            else:
                current_user = request.user
                current_user.set_password(new1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                messages.success(request, 'Password Successfully Changed')
                return redirect('dashboard')
        else:
            messages.warning(request, 'Wrong Old Password, Please Try Again')
            return redirect('change-password')
    return render(request, 'users/change_password.html', context=context)
