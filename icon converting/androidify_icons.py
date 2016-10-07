import os, shutil

drawable_folder = 'drawable'

def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.png')]
    print(files)
    return files

def find_out():
    out_folder = 'out'
    counter = 0;
    while os.path.exists(out_folder + (str(counter) if counter != 0 else '')):
        counter += 1
    out_folder += (str(counter) if counter != 0 else '')
    print('Out folder:', out_folder)
    return out_folder

def make_folders(out_folder):
    os.mkdir(out_folder)
    os.chdir(out_folder)
    densities = {'ldpi':0, 'mdpi':1, 'hdpi':1, 'xhdpi':1, 'xxhdpi':1, 'xxxhdpi':1}  # 0.75, 1, 1.5, 2, 3, 4. Turn on/off with 1 and 0.
    enabled = {key: densities[key] for key in densities if densities[key] == 1}
    for key in enabled:
        os.mkdir(drawable_folder+'-'+key)
    os.chdir('..')
    return enabled

def correct_name(name):
    densities = {0.75:'ldpi', 1:'mdpi', 1.5:'hdpi', 2:'xhdpi', 3:'xxhdpi', 4:'xxxhdpi'}
    scale = 1
    if '@' in name:
        position = name.find('@')
        scale = name[position + 1 : -5]
        scale = scale.replace(',','.')
        scale = float(scale)
        name = name[:position] + name[-4:]
    name = name.replace('-', '_')
    name = name.lower()

    if scale in densities:
        density = densities[scale]
    else:
        print('Invalid scale found:',name,density)
        raise ValueError('Invalid scale '+str(density)+'.')

    return (name, density)

def copy_files(files, destination):
    for f in files:
        new_name = files[f][0]
        density = files[f][1]
        folder = drawable_folder + '-' + density
        path = os.path.join(destination, folder, new_name)
        print('Moving',f,'to destination',path)
        shutil.copy(f, path)

if __name__ == '__main__':
    files = list_files()
    path = find_out()
    make_folders(path)
    new_files = {f:correct_name(f) for f in files}  # {"Cross.png":(cross.png, mdpi)}
    print('File mapping:\n',new_files)
    copy_files(new_files, path)
    print('Done.')
