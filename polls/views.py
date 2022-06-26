from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import redirect, render

def index(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        da1 = request.POST.get("qr_text1")
        da2 = request.POST.get("qr_text2")
        da3 = str(da1) + str(da2)
        print(da3) 
        img = qrcode.make(request.POST.get(da3), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()



    return render(request, "index.html", context=context)
