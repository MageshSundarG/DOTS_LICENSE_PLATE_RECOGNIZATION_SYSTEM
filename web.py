from detect import main as di
from detect_video import main as dv
from core.utils import recognize_plate,draw_bbox


def detect_image(img):
    di.main(_argv)
    img,coor = draw_bbox(_argv)
    plate_num = recognize_plate(img,coor)

    return plate_num


def detect_video(video):
    dv.main(_arg)
    img,coor = draw_bbox(_argv)
    plate_numlist = recognize_plate(img,coor)

    return plate_numlist