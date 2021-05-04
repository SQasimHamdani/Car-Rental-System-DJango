from PIL import Image
from datetime import datetime
import pytz

utc=pytz.UTC

def resize_car_image(image_path):
    # print('image resize call')

    preffered_image_size = [600,400]
    img = Image.open(image_path)
    width, height = img.size  # Get dimensions

    # if width > preffered_image_size[0] and height > preffered_image_size[1]:
    #     # keep ratio but shrink down
    #     img.thumbnail((width, height))

    # check which one is smaller
    # if height < width:
    #     # make square by cutting off equal amounts left and right
    #     left = (width - height) / 2
    #     right = (width + height) / 2
    #     top = 0
    #     bottom = height
    #     img = img.crop((left, top, right, bottom))

    # elif width < height:
    #     # make square by cutting off bottom
    #     left = 0
    #     right = width
    #     top = 0
    #     bottom = width
    #     img = img.crop((left, top, right, bottom))
    
    if width > preffered_image_size[0] and height > preffered_image_size[1]:
        img.thumbnail((preffered_image_size[0], preffered_image_size[1]))

    img.save(image_path)
    """
    # img = Image.open(self.car_photo.path) # Open image using self
        
    # recommeded_img_h = 720
    # recommeded_img_w = 1080

    # img_h = img.height
    # img_w = img.width

    # if img.height > recommeded_img_h : 
    #     img_h = int(img_h * ( recommeded_img_h / img_h ))
    #     # print('height resized to ',img_h)
        
    # if img.width > recommeded_img_w :
    #     img_w = int(img_w * ( recommeded_img_w / img_w ))
    #     # print('width resized to ',img_w)
        
    # new_img = (img_h, img_w)
    # # print(new_img)
    # # img.thumbnail(new_img)
    
    # # cropped_image = image.crop((x, y, w+x, h+y))
    # img = img.resize(new_img, Image.ANTIALIAS)
    # img.save(self.car_photo.path)  # saving image at the same path
    """
def check_booking_availability(SaleOrder,Car,search_parameters):
    bookings = SaleOrder.objects.all()
    cars = Car.objects.all()

    available_cars = []
    for booking in bookings:
        # print()
        # 2021-05-02 18:31:27.000000
        format_string = "%d %b"
        picking_date = search_parameters["picking_date"]
        print(picking_date)
        picking_date = datetime.strptime(picking_date, format_string)

        return_date = search_parameters["return_date"]
        return_date = datetime.strptime(return_date, format_string)
        
        if booking.Order_Date > picking_date and booking.Deliver_Date < return_date:
            available_cars.append(True)
        else:
            available_cars.append(False)
        return any(available_cars)

