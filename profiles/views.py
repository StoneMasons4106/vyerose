from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from django.contrib.auth.models import User
from products.models import Category
from allauth.account.models import EmailAddress

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        form_two = UserForm(request.POST, instance=user)
        if form.is_valid() and form_two.is_valid():
            try:
                user_email = get_object_or_404(EmailAddress, user_id=request.user)
                if request.POST.get('email') != user_email:
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
    categories = Category.objects.values()

    template = 'profiles/profile.html'
    context = {
        'page': 'profile',
        'profile': profile,
        'user': user,
        'orders': orders,
        'on_profile_page': True,
        'categories': categories,
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
    categories = Category.objects.values()
    
    context = {
        'page': 'profile',
        'form': form,
        'form_two': form_two,
        'orders': orders,
        'on_profile_page': True,
        'categories': categories,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    categories = Category.objects.values()

    context = {
        'page': 'profile',
        'order': order,
        'from_profile': True,
        'categories': categories,
    }

    return render(request, template, context)