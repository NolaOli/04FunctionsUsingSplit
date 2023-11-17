def meal_time(timestring):
  hours, minutes = timestring.split(":")

  hours = int(hours) 
  minutes = int(minutes)

  if hours >= 7 and hours <= 8:
    return "Breakfast"
  elif hours >= 12 and hours <= 13:
    return "Lunch"
  elif hours >= 18 and hours <= 19:
    return "Dinner"
  else:
    return "No meal currently."

print("07:00 =>", meal_time("07:30"))
print("18:00 =>", meal_time("18:30"))
print("08:00 =>", meal_time("08:30"))
print("13:00 =>", meal_time("13:15"))
print("19:00 =>", meal_time("19:25"))
print("14:00 =>", meal_time("14:35"))


def get_filename_extension(filename):
  file, extension = filename.split(".")

  file = file
  extension = extension
  
  return extension

print("data.csv =>", get_filename_extension("data.csv"))
print("woop.pop =>", get_filename_extension("woop.pop"))
print("wopy.kip =>", get_filename_extension("wopy.kip"))


def is_image_file(filename):
  file, extension = filename.split(".")

  file = file
  extension = extension

  if extension == "jpg":
    return True 
  elif extension == "jpeg":
    return True
  elif extension == "png":
    return True
  elif extension == "gif":
    return True
  elif extension == "tiff":
    return True
  else:
    return "Not an image file."

print("skippy.jpg =>", is_image_file("skippy.jpg"))
print("skop.csv =>", is_image_file("skop.csv"))
print("tiffiany.tiff =>", is_image_file("tiffiany.tiff"))