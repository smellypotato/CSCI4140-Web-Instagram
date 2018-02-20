# CSCI4140-Web-Instagram
Website link: http://web-ig-potato-web-instagram.7e14.starter-us-west-2.openshiftapps.com
Inilization link: http://web-ig-potato-web-instagram.7e14.starter-us-west-2.openshiftapps.com/init.html

## Directories
### cgi-bin
stores all the cgi scripts
### upload
stores all uploaded images, public images with permalink will be stored as upload/file_name
### upload/filter
stores public images during editing, images in this directory will be deleted if not in editor page
### upload/thumbnail
stores thumbnails of the public images with permalink
### upload/username
stores all private uploaded images with permalink
### upload/username/filter
stores private images during editing, images in this directory will be deleted if not in editor page
### upload/username/thumbnail
stores thumbnails of the private images with permalink

## Files
## image.db
stores information of images with permalink
## account.db
stores information of user accounts

## Implementation procedure
Spent around 3 days to configure openshift
Built the application on local host with Python 2.7
Chose sqlite3 as database package
Implement access control and session management function
Implement file upload function
Tried to use pythonmagick api
Implement editor and filter function (except lomo filter)
Realise it cannot create lomo filter
Implement pagination function
Implement initialization function
Deployed the application on Openshift
Replace pythonmagick with ImageMagick

## Functionality Remark
An image can add as many filter as you like, but it can only undo once.
Inilialization will remove all images and reset all databases
Sign up will automatically sign in if success


## Good/Bad
Overall bad, i don't deserve any bonus  
Initialization cannot implement with authorization due to unknown reason, anyone with the url can initialize the system  
In editor mode, effect of lensflare filter is visible with image dimension bigger than 250x250. Please compare it with original image if the effect is not clear. I don't have time to learn how to get values from subprocess. Also, if the first time lensflares is not applied to the image, please apply the filter again and it should work  
In editor mode, effect of black & white filter only change the image to grayscale without the gradient filter. It works when I use pythonmagick but doesn't work with Imagemagick.  
Update account allows update with old password  
Account creation allows any kind of input (spaces, number, alphabets, special symbols, any length..)  

I have spent 2 weeks working on only this assignment and I only have 2 more days before holiday end so I can't do any more improvements
