import os, shutil
from PIL import Image, ImageOps


out_folder_prefix = 'out'
pixel_scales = {"ldpi": 0.75, "mdpi": 1, "hdpi":1.5, "xhdpi":2, "xxhdpi":3, "xxxhdpi":4}
padding_dp = 4  # pixels to add, for a mdpi image. Scaled for other sizes
padding_percent = 0.125
padding_use_percent = True  # switch between dp and percent here


def find_out():
    out_folder = out_folder_prefix
    counter = 0;
    while os.path.exists(out_folder + (str(counter) if counter != 0 else '')):
        counter += 1
    out_folder += (str(counter) if counter != 0 else '')
    print('Out folder:', out_folder)
    return out_folder

def find_density(filename):
    density = 1
    if '-' in filename:
        filename = filename.split('-')[1]
        for key in pixel_scales:
            if key == filename:
                density = pixel_scales[key]
                break
    return density

def list_all_files():
    ''' returns a dict with {filepath: density} and a list of folders with images'''
    files = {}
    folders = {}
    for node in os.walk("."):
        # node is (path, folders, files) tuple
        current_folder = node[0]
        if out_folder_prefix in current_folder:
            continue

        current_files = node[2]
        if len(current_files):
            for f in current_files:
                if f.endswith(".png"):
                    path = os.path.join(current_folder, f)
                    density = find_density(current_folder)
                    files[path] = density
                    folders[current_folder] = current_folder  # lazy way of making a set, lol
    return files, [f for f in folders if f != "."]

def process_image(filepath, pixel_scale, out_folder):
    im = Image.open(filepath)

    if padding_use_percent:
        max_size = max(im.width, im.height)  # use relative padding, since we get weird dimensions from our designer
        border = pixel_scale * padding_percent * max_size  # must be int, so expand does not crash
    else:
        border = pixel_scale * padding_dp
    border = int(round(border))

    print("Editing",filepath,im.size,im.format,im.mode,"\n\tAdding ",border,"pixels.")
    im_expanded = ImageOps.expand(im, border)
    path = os.path.join(out_folder, filepath)
    im_expanded.save(path)

    im.close()
    im_expanded.close()

def make_folders(out, folders):
    os.mkdir(out)
    os.chdir(out)
    for folder in folders:
        os.mkdir(folder)
    os.chdir('..')


if __name__ == '__main__':
    out = find_out()  # destination folder for edited images
    files, folders = list_all_files()  # ({filename: density}, [folders])
    print("Found images in:",folders)
    print("\n\nAll images:",files,"\n","="*50,"\n")
    make_folders(out, folders)

    for f in files:
        process_image(f, files[f], out)
    print('Done! Expanded',len(files),'images.')
