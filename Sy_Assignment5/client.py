#Test the model with test images
#here are some images located at: https://oreil.ly/dEUpx
#you can try your own images. note: the model is training on images with whitebackground
import sys
import requests

if(len(sys.argv) > 1):
    r = requests.get('http://localhost')
    print(r.text)

    inputfile = sys.argv[1]
    """ post image and return the response """
    my_img = {'image': open(inputfile, 'rb')}
    r = requests.post('http://localhost/ml', files=my_img)
    print(r.text)

else:
    r = requests.get('http://localhost')
    print(r.text)
