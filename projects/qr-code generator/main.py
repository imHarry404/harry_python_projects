import qrcode
# pip3 install qrcode -> to install this library


# creatring objects 
qr=qrcode.QRCode(
    version=15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size=10, #10 means the box where qr code will be displayed
    border=5 #it is the white part of image -> border in all 4 sides with white border      
)
# data='https://www.linkedin.com/in/imharry404/'
# data='hiii this is harry' 
#here we can give any link or anything , any text message,any link 


# passing data to the object
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
#this is save the image in the current directory
img.save('message.png')  #filename for your qr code


# lets run it, it will create a qr code image, after scanning it you can find my linkedIn account

# after scanning that image LinkedIn account can be access



# imharry404

# after scanning that code it will show that message ,,thanks :)
