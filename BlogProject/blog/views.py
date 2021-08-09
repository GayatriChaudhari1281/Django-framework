from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from blog.forms import EmailSendForm,CommentsForm
from taggit.models import Tag
# Create your views here.
def PostList_view(request,tag_slug=None):
    #post_list=Post.objects.all()
    post_list=Post.objects.filter(status__exact='published')
    tag=None
    if tag_slug:#if tag_slug is not none
        tag=get_object_or_404(Tag,slug=tag_slug)#
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')#page is predefined word
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list,'tag':tag})


def PostDetail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)#comments is canonical name in models
    csubmit=False
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            #wwe cannot call save method directly because we are sending 3 fields only but there are too many  fields in databases
            new_comment=form.save(commit=False)
            new_comment.post=post#here we are associating the comment with the related post in database
            new_comment.save()
            csubmit=True
    else:
        form=CommentsForm()
    return render(request,'blog/postdetail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({})recommends you to read "{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post At:\n{}\n\n{}\'s comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'gayatri.chaudhari1281@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blog/sharebyemail.html',{'form':form,'post':post,'sent':sent})
