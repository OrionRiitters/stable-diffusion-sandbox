from pipes.basic import usePipe, basicPipe
import datetime

image = usePipe(basicPipe(), "a gimmick", 9, 2, 1024)
imageName = "./out/gimmick/img"+str(datetime.datetime.now().timestamp())+".png"
image.save(imageName)

