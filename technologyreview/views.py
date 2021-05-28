# from django.shortcuts import render,HttpResponse
#
# def test(request):
#     url='https://hindi.gizbot.com/gadgets/amazfit-will-launch-gt0-gtr-2e-and-gts-2e-on-19th-jan-features-specifications-and-price-020114.html'
#     r=requests.get(url)
#     htmlcontent=r.content
#     soup=BeautifulSoup(htmlcontent,'html.parser')
#     # print(soup.prettify)
#     content=soup.find_all('p')
#     # print(content.get_text())
#     a=''
#     for i in content:
#         a=a+i.get_text()
#
    # return HttpResponse(a)
