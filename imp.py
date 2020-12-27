import os
folder =  "sdcard/mdict/doc/"
for root, dirs, files in os.walk("D:\\mdict\\docx\\"):
  for name in files:
    path = os.path.join(root, name)
    print(path)
    target_path = folder + path.replace("D:\\mdict\\docx\\", '').replace("\\", '/') 
    target_dir = target_path.replace(name, "")
    if target_dir != folder:
      os.system(f'C:\\adb\\adb.exe shell mkdir "{target_dir}"')
    command = 'C:\\adb\\adb.exe push "' + path + '" "' + target_path + '"'
    print("--- " + command)
    os.system(command)
