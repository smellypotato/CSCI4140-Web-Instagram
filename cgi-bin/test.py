import os
import PythonMagick as pm
path = os.path.dirname(os.getcwd()) + '\upload\DSC_1019.png'
image = pm.Image(path)
print image.boxColor
