from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)
    
    try:
        social_account = get_object_or_404(SocialAccount, user_id=request.user)
    except:
        social_account = False

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        form_two = UserForm(request.POST, instance=user)
        if form.is_valid() and form_two.is_valid():
            try:
                user_email = get_object_or_404(EmailAddress, user_id=request.user)
                if str(request.POST.get('email')) != str(user_email):
                    new_email = request.POST.get('email')
                    profile.add_email_address(request, new_email)
                    messages.success(request, 'Profile updated successfully, please confirm the new email in your profile by clicking the link in the email sent to you.')
                else:
                    messages.success(request, 'Profile updated successfully.')
                form.save()
                form_two.save()
            except EmailAddress.MultipleObjectsReturned:
                messages.error(request, 'Please confirm the email in your profile before attempting to update it again.')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        form_two = UserForm(instance=user)
    
    orders = profile.orders.all() 
    
    template = 'profiles/profile.html'
    context = {
        'page': 'profile',
        'profile': profile,
        'user': user,
        'orders': orders,
        'on_profile_page': True,
        'social_account': social_account,
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    form = UserProfileForm(instance=profile)
    form_two = UserForm(instance=user)
    orders = profile.orders.all()

    messages.info(request, f'You are now editing your profile.')
    template = 'profiles/edit_profile.html'
    
    context = {
        'page': 'profile',
        'form': form,
        'form_two': form_two,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    '''Delete user profile'''
    if request.method == "POST":
    
        user = get_object_or_404(User, username=request.user)
        user.delete()

        messages.success(request, 'You have successfully deleted your profile.')
        return redirect(reverse('home'))
    
    template = "profiles/delete_profile.html"

    context= {
        'page':'profile',
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'

    context = {
        'page': 'profile',
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)