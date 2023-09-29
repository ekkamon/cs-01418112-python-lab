fileName = str(input())

forbidden = [' ', '.', '\\', '/', '*', ':', '|', '"', '<', '>']

def get_extension_idx():
  return fileName.rfind('.')

def set_file_name():
  result = ''
  extension_idx = get_extension_idx()

  for idx in range(len(fileName)):
    val = fileName[idx]

    if val in forbidden and idx != extension_idx:
      result += '_'
    else:
      result += val

  return result

def is_have_extension(fileName):
  return True if fileName.count('.') == 1 else False

fileName = set_file_name()

if is_have_extension(fileName):
  name, extension = fileName.split('.')
  print(f'{name[:15]}.{extension[:3]}')
else:
  print(fileName[:15])