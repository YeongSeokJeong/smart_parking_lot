import io
import socket
import struct
from PIL import Image
from datetime import datetime, timedelta

def server_action() :
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8003))
    server_socket.listen(1)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')

    try:
        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop

        
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            print('Image is %dx%d' % image.size)

            path = '/home/parking_lot/section4/'
            fname = '[Sec4]'+ datetime.today().strftime("%Y-%m-%d-%H%M%S") + ".jpg"
            image.save(path + fname)
            print('Sec4 Image is saved in ' + path)
            print('File name : ' + fname)
            image.verify()
            print('Sec4 Verify Success')
    finally:
        connection.close()
        server_socket.close()
server_action()
