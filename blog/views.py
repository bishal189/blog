from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Post,Author,Tag
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import SpecificForm
from.models import comment
from django.urls import reverse


class List(ListView):
    template_name='blog/index.html'
    model=Post
    ordering = ['-date']
    def get_queryset(self):
        get_objects=Post.objects.all()[:3]
        return get_objects

class Postview(View):
    def get(self,request):
        all_post=Post.objects.all()
        content={
        'all_posts':all_post
        
    }
        return render(request,'blog/all_post.html',content)





class Detail(View):
    def get(self,request,slug):
        get_object=Post.objects.get(slug=slug)
        stored_post=request.session.get('stored_posts')
       
        if stored_post is not None:
            later_button=get_object.id in stored_post
            print(stored_post)
            print(later_button,'******************')
            

        else:
            later_button=False



        context={
            'object':get_object,
            'comment_form':SpecificForm(),
            'tags':get_object.caption.all(),
            'data':get_object.comment.all().order_by('-id'),
            'later_button':later_button
        }
        return render(request,'blog/post_details.html',context)
    def post(self,request,slug):    
       data=SpecificForm(request.POST)
       get_object=Post.objects.get(slug=slug)

       stored_post=request.session.get('stored_posts')
       if stored_post is not None:

        later_button= Post.id in stored_post

       else:
        later_button=False

       if data.is_valid():
        print('valid')
        comment=data.save(commit=False)
        comment.post=get_object
        comment.save()
        
        return HttpResponseRedirect(reverse('specific_post', args=[slug]))


       
       context={
            'object':get_object,
            'comment_form':data,
            'tags':get_object.caption.all(),
            'data':get_object.comment.all().order_by('-id'),
            'later_button':later_button
        }
       return render(request,'blog/post_details.html',context)

#using session here to implement read later feature imp//
class Readlater(View):
    def get(self,request):
        stored_posts=request.session.get('stored_posts')
        print(stored_posts)
        context={

        }

        if stored_posts is None or len(stored_posts)==0:
            context['posts']=[]
            context['has_post']=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            print(posts)
            context['posts']=posts
            context['has_post']=True

        return render(request,'blog/stored.html',context)        





    def post(self,request):
        stored_posts=request.session.get('stored_posts')
        print(stored_posts,'******** post')#returns none
        if stored_posts is None:
            stored_posts=[]

        get_id=int(request.POST['post_id']  )
        if get_id not in stored_posts: 
           stored_posts.append(int(get_id)) 
           request.session['stored_posts']=stored_posts


        else:
            stored_posts.remove(get_id)
        request.session['stored_posts']=stored_posts       
        return HttpResponseRedirect('/')
