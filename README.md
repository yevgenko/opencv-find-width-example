

Sensor script:
l_sensor_base = X (constant)
l_object = l_sensor_base - l_sensor_object

Camera script:
l_object = X (input by user)
l_camera_base = X (constant)
l_camera_to_object = l_camera_base - l_object

How to get width and height?
marker[1][0] # width
perhaps `marker[1][1]` # is height?
