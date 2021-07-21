import numpy as np
import cv2

def matrix2uint (matrix, in_bit = 16, out_bit= 8, out_dtype = np.uint8):
    """
    matrix : array
    in_bit: bit of input array, dtype= int
    out_bit: bit of output array, dtype= int
    out_dtype: numpy dtype of output array, ex) np.uint8, np.uint16 ...
    """
    m_min= 0
    m_max= 2**in_bit-1
    matrix=matrix-m_min
    output= (np.array (np.rint((matrix-m_min)/float (m_max-m_min) * (2**out_bit-1)), dtype=out_dtype))
    return output

def resize_image(imageSize, in_arr, channel=False, in_out_channel_same=True, dtype = np.uint8):
    """
    imageSize, in_arr, channel=False, in_out_channel_same=True, dtype = np.uint8
    """
    img_stand = max(in_arr.shape)
    img=in_arr
    scale = imageSize/img_stand

    # imageSize = reSize
    if channel == False:
        imgnpy = np.zeros((imageSize,imageSize), dtype=dtype)

        if img_stand == img.shape[0]:
        # print('here')
            resized = cv2.resize(in_arr, dsize=(round((img.shape[1]/img_stand)*imageSize),imageSize), interpolation=cv2.INTER_AREA)
            imgnpy[:imageSize,:round((img.shape[1]/img_stand)*imageSize)] = resized[:,:]
        else:
            resized= cv2.resize(in_arr, dsize=(imageSize,round((img.shape[0]/img_stand)*imageSize)), interpolation=cv2.INTER_AREA)
            imgnpy[:round((img.shape[0]/img_stand)*imageSize),:imageSize] = resized[:,:]
    else:
        imgnpy = np.zeros((imageSize,imageSize,3), dtype=dtype)

        
        if in_out_channel_same==True:
            if img_stand == img.shape[0]:
                
                # print('here')
                resized = cv2.resize(in_arr, dsize=(round((img.shape[1]/img_stand)*imageSize),imageSize), interpolation=cv2.INTER_AREA)
                imgnpy[:imageSize,:round((img.shape[1]/img_stand)*imageSize),:] = resized[:,:,:]
            else:
                resized= cv2.resize(in_arr, dsize=(imageSize,round((img.shape[0]/img_stand)*imageSize)), interpolation=cv2.INTER_AREA)
                # imgnpy[:round((img.shape[1]/img_stand)*imageSize),:imageSize,:] = resized[:,:,:]
                imgnpy[:round((img.shape[0]/img_stand)*imageSize),:imageSize,:] = resized[:,:,:]



        else:
            if img_stand == img.shape[0]:
                
                for a in range(3):
                    resized = cv2.resize(in_arr, dsize=(round((img.shape[1]/img_stand)*imageSize),imageSize), interpolation=cv2.INTER_AREA)
                    imgnpy[:imageSize,:round((img.shape[1]/img_stand)*imageSize),a] = resized[:,:]
            else:

                for a in range(3):
                    resized= cv2.resize(in_arr, dsize=(imageSize,round((img.shape[0]/img_stand)*imageSize)), interpolation=cv2.INTER_AREA)
                    imgnpy[:round((img.shape[0]/img_stand)*imageSize),:imageSize,a] = resized[:,:]
    return imgnpy, scale