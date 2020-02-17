from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse

import json
from .models import Bee_robot

# render current available bee list descendingly
def index(request):
    bee_robot_list = Bee_robot.objects.order_by('-id')
    context = {
        'bee_robot_list': bee_robot_list,
    }
    return render(request, 'simple_bee/index.html', context)

# render the target bee's stats
def detail(request, bee_robot_id):
    bee_robot = get_object_or_404(Bee_robot, pk=bee_robot_id)
    context = {
        'bee_robot': model_to_dict(bee_robot),
    }
    return render(request, 'simple_bee/detail.html', context)

# render the register form
def register(request):
    fields = Bee_robot._meta.get_fields()
    fields = [str(f).split(".")[2] for f in fields]
    context = {
        'fields': fields[1:],
    }
    return render(request, 'simple_bee/register.html', context)

# receive request.POST and populate a new bee accordingly
# WARNING: this function is not thoroughly tested! Input unsupported data will cause unpredicted behavior!
def register_confirm(request):
    NECTAR = request.POST['nectar'] if request.POST['nectar'] != "" else 0
    HONEY = request.POST['honey'] if request.POST['honey'] != "" else 0
    FUEL = request.POST['fuel'] if request.POST['fuel'] != "" else 100
    DAMAGE = request.POST['damage'] if request.POST['damage'] != "" else 0
    SPEED = request.POST['speed'] if request.POST['speed'] != "" else 1
    LATITUDE = request.POST['latitude'] if request.POST['latitude'] != "" else 0
    LONGITUDE = request.POST['longitude'] if request.POST['longitude'] != "" else 0
    ELEVATION = request.POST['elevation'] if request.POST['elevation'] != "" else 0
    STATUS = request.POST['status'] if (request.POST['status'] < 3 and request.POST['status'] >= 0) else 0
    IS_ACTIVE = True if request.POST['is_active'] > 0 else False
    
    new_bee = Bee_robot(nectar=NECTAR, 
                        honey=HONEY, 
                        fuel=FUEL, 
                        damage=DAMAGE, 
                        speed=SPEED, 
                        latitude=LATITUDE, 
                        longitude=LONGITUDE, 
                        elevation=ELEVATION,
                        elevation=IS_ACTIVE
                        )
    new_bee.save()
    return HttpResponseRedirect(reverse('simple_bee:detail', args=(new_bee.id,)))

# change the active state of the target bee.
# WARNING: any http request is received! Not only POST!
def decommission(request, bee_robot_id):
    bee_robot = get_object_or_404(Bee_robot, pk=bee_robot_id)
    bee_robot.is_active = not bee_robot.is_active
    bee_robot.save()
    context = {
        'bee_robot': model_to_dict(bee_robot),
    }
    return HttpResponseRedirect(reverse('simple_bee:detail', args=(bee_robot_id,)))

# delete the active state of the target bee.
# WARNING: any http request is received! Not only DELETE!
def delete(request, bee_robot_id):
    bee_robot = get_object_or_404(Bee_robot, pk=bee_robot_id)
    bee_robot.delete()
    return HttpResponseRedirect(reverse('simple_bee:index'))

# change the state of the target bee.
# WARNING: any http request with correct body is received! Not only PUT!
def put(request, bee_robot_id):
    bee_robot = get_object_or_404(Bee_robot, pk=bee_robot_id)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(bee_robot_id, body)

    if not bee_robot.is_active or len(body) == 0:
        return HttpResponseRedirect(reverse('simple_bee:index'))

    for key in body:
        value = body[key]
        if key == "nectar":
            bee_robot.nectar = int(value)
        elif key == "honey":
            bee_robot.honey = int(value)
        elif key == "fuel":
            bee_robot.fuel = int(value)
        elif key == "damage":
            bee_robot.damage = int(value)
        elif key == "status":
            bee_robot.status = int(value)
        elif key == "speed":
            bee_robot.speed = float(value)
        elif key == "latitude":
            bee_robot.latitude = float(value)
        elif key == "longitude":
            bee_robot.longitude = float(value)
        elif key == "elevation":
            bee_robot.elevation = float(value)


    bee_robot.save()
    return HttpResponseRedirect(reverse('simple_bee:index'))

# render random data page
def random(request):
    bee_robot_list = Bee_robot.objects.order_by('-id')
    json_list = [b.as_json() for b in bee_robot_list]
    json_list = json.dumps(json_list)

    context = {
        'bee_robot_list': bee_robot_list,
        'json_list': json_list
    }
    return render(request, 'simple_bee/random.html', context)

# respond GET request with target bee robot json
def get(request, bee_robot_id):
    bee_robot = get_object_or_404(Bee_robot, pk=bee_robot_id)
    response = JsonResponse(model_to_dict(bee_robot))
    return response
