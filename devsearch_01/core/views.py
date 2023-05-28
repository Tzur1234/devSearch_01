from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from devsearch_01.core.forms import UserDetailForm
from django.contrib.auth.decorators import login_required



# Create your views here.

# Account

@login_required
def account_detail(request, pk):
    '''
        # GET # 

        Input: request ojbect about and PK representing 
        the user's primery Key

        OutPUt: returns the account.html with the user's details

        # POST #
    
    '''
    
    
    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        initial_data = {
            'name':user.account.name ,
            'title': user.account.title ,
            'about': user.account.about ,
            'profile_image': user.account.profile_image,
            'location': user.account.location
        }

        form = UserDetailForm(initial=initial_data)
    
    if request.method == 'POST':
        # Authorize the user
        if request.user.id == pk:
            # get the form
            form = UserDetailForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                title = form.cleaned_data['title']
                about = form.cleaned_data['about']
                profile_image = form.cleaned_data['profile_image']
                location = form.cleaned_data['location']

                # Update the database
                account = request.user.account
                      
                account.name = name
                account.title = title
                account.about = about
                if profile_image != None:
                    account.profile_image = profile_image
                account.location = location
                account.save()

            print('errors:' ,type(form.errors))

    context = {
    'receive_pk': pk,
    'user': user,
    'form': form,
    }
    print('Return the account.html page')
    return render(request, 'pages/account.html', context)
        

