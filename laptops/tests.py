from django.test import TestCase
from .models import Laptop
# Create your tests here.

#Test case creates a sample database and performs tests based on the sample database.
class LaptopModelTest(TestCase):
    def setUp(self):
        Laptop.objects.create(typ="Programming",brand="HP",model="Elitebook",price=55000,weight=2.2,size=14.4,color="Silver",processorBrand="Intel", processorModel="i Core 5", ram="4",storageType="HDD",storageMemory="256GB", batteryLife=14,graphicsCardBrand="NVidia",graphicsCardModel="GEForce",graphicsMemory=4,os="Windows 10",office="MS Office 2016", extraInfo="X info",pros="pros",cons="cons",amazonLink="www.amazon.com",flipkartLink="www.flipkart.com",img1="5678d84c3e198af1931120be8693681c.jpg",img2="5678d84c3e198af1931120be8693681c.jpg",img3="5678d84c3e198af1931120be8693681c.jpg",img4="5678d84c3e198af1931120be8693681c.jpg",img5="5678d84c3e198af1931120be8693681c.jpg",img6="5678d84c3e198af1931120be8693681c.jpg")
        
    def test_text_content(self):
        l = Laptop.objects.get(id=1)
        expected_object_name = l.img6
        self.assertEqual(expected_object_name,"5678d84c3e198af1931120be8693681c.jpg")