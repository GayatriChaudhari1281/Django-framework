from django.shortcuts import render
from demoapp.models import Employee
from django.db.models import Q,Avg,Max,Min,Count,Sum
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all()#django ORM
    #employee=Employee.objects.get(id=10)#django ORM
    #employee=Employee.objects.filter(esal__gt=222995.0)#__gt magic methods
    #employee=Employee.objects.filter(esal__gte=222995.0)
    #employee=Employee.objects.filter(esal__lt=222995.0)
    #employee=Employee.objects.filter(esal__lte=222995.0)#for block- filter function to get more record
    #employee=Employee.objects.filter(id__exact=14)
    #employee=Employee.objects.get(ename__exact='Joseph Keith')
    #employee=Employee.objects.get(ename__iexact='joseph Keith')#i=>insensitive
    #employee=Employee.objects.filter(ename__contains='John')#if block- get function to get one name
    #employee=Employee.objects.filter(ename__icontains='jo')
    #employee=Employee.objects.filter(id__in=[76,7,4,29,56,21,67,32,98])
    #employee=Employee.objects.filter(ename__startswith='r')#no need of istartswith it is byddefault insensitive
    #employee=Employee.objects.filter(ename__endswith='r')
    #employee=Employee.objects.filter(esal__range=(184929,300000))
    #employee=Employee.objects.filter(esal__range=(183229,240000))|Employee.objects.filter(ename__startswith='j')#logical operator in database and ,or
    #employee=Employee.objects.filter(esal__range=(183229,240000))&Employee.objects.filter(ename__startswith='j')
    #employee=Employee.objects.filter(Q(esal__range=(183229,240000))&Q(ename__startswith='j'))
    #employee=Employee.objects.filter(Q(esal__range=(183229,240000))|Q(ename__startswith='j'))
    #employee=Employee.objects.filter(esal__range=(183229,240000),ename__startswith='j')
    #employee=Employee.objects.exclude(esal__range=(180000,240000))#not function
    #employee=Employee.objects.filter(~Q(esal__range=(180000,240000)))#not function
    #employee=Employee.objects.exclude(ename__startswith='c')
###UNION Function
    #employee1=Employee.objects.filter(esal__lt=170000)
    #employee2=Employee.objects.filter(ename__startswith='c')
    #employee3=employee1.union(employee2)#it returns single queryset
    #employee=Employee.objects.all().values('ename','esal')
    #employee=Employee.objects.all().only('ename','esal')
###AGGREGATE
    #avg=Employee.objects.all().aggregate(Avg('esal'))
    #max=Employee.objects.all().aggregate(Max('esal'))
    #min=Employee.objects.all().aggregate(Min('esal'))
    #sum=Employee.objects.all().aggregate(Sum('esal'))
    #count=Employee.objects.all().aggregate(Count('esal'))
    #my_dict={'avg':avg,'max':max,'min':min,'sum':sum,'count':count}
    #return render(request,'demoapp/aggregate.html',my_dict)

    #employee=Employee(eno=1234,ename="Gayatri",esal=94539452,eaddress="Om Sai Nagar,Chopda")

    #employee=Employee.objects.all().order_by('eno')
####CREATE
    #employee=Employee(eno=1234,ename='Rahul',esal=95000,eaddress='Pusad')
    #employee.save()
##bulk creation
    #e1=Employee(eno=456,ename='Dhiraj',esal=95000,eaddress='Pusad')
    #e2=Employee(eno=95,ename='Gayatri',esal=5677,eaddress='Pusad')
    #employee=Employee.objects.bulk_create([e1,e2])
###delete records:
    #e=Employee.objects.get(ename='Dhiraj')
    #e.delete()
    #e=Employee.objects.filter(esal__lt=25000)
    #e.delete()
    #employee=Employee.objects.all().delete()
###update
    #e=Employee.objects.get(id=322)
    #e.ename='Sehwag'
    #e.save()
##sorting
    #employee=Employee.objects.all().order_by('-eno')
    #employee=Employee.objects.all().order_by('-esal')[0:10]
    employee=Employee.objects.all().order_by('ename')
    
    #employee=Employee.objects.all()
    my_dict={'emp':employee}

    #print(type(employee))
    return render(request,'demoapp/index.html',my_dict)
